"""
AI-driven SEO metadata generation module with multi-provider support
"""

import os
from typing import Dict, Optional, Tuple, List, Any
import openai
import google.generativeai as genai
import anthropic
from dotenv import load_dotenv
import logging
from enum import Enum
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from .cost_calculator import CostCalculator
from .config import ENDPOINT_MAP, POST_TYPE_CONTEXT, DEFAULT_CONFIG, RegionConfig, Config
from urllib.parse import urlparse
from time import sleep
import langdetect
from langdetect import DetectorFactory
import json
from datetime import datetime
import re
import spacy
from collections import Counter
from textblob import TextBlob

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Set seed for consistent language detection
DetectorFactory.seed = 0

class AIProvider(Enum):
    DEEPSEEK = "deepseek"
    OPENAI = "openai"
    GOOGLE = "google"
    ANTHROPIC = "anthropic"

class MetadataGenerator:
    """Generates SEO metadata for content using AI providers."""
    
    def __init__(self, config: Config) -> None:
        self.config = config
        self.current_provider = None
        self.current_model = None
        self.last_cost = 0.0
        self.last_input_tokens = 0
        self.last_output_tokens = 0
        self.last_total_tokens = 0
        self.provider = config.provider or os.getenv('PREFERRED_AI_PROVIDER', 'google')
        self.model = None
        self.cost_calculator = CostCalculator()
        self.language = config.language  # Store the forced language if provided
        self.region_config = config.region_config
        # RankMath recommended limits
        self.title_max_length = 60  # Recommended for Google SERP display
        self.title_absolute_max = 70  # Absolute maximum allowed by RankMath
        self.description_max_length = 155  # Recommended for Google SERP display
        self.description_absolute_max = 320  # Absolute maximum allowed by RankMath
        self.keyword_min_length = 3
        self.keyword_recommended_count = 3  # Recommended number of focus keywords
        self.keyword_max_count = 10  # Arbitrary limit for safety
        self.used_keywords = set()  # Track used keywords to avoid repetition
        logger.debug(f"Initializing MetadataGenerator with provider: {self.provider}")
        self._initialize_provider()
        # Load spaCy model for NLP
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except Exception as e:
            logger.error(f"Error loading spaCy model: {str(e)}")
            self.nlp = None

    def _initialize_provider(self):
        """Initialize the selected AI provider with appropriate credentials"""
        try:
            # Ensure provider value matches AIProvider enum
            valid_providers = [p.value for p in AIProvider]
            logger.debug(f"Valid providers: {valid_providers}")
            logger.debug(f"Current provider: {self.provider}")
            
            if self.provider not in valid_providers:
                raise ValueError(f"Unsupported AI provider: {self.provider}. Options: {', '.join(valid_providers)}")
                
            if self.provider == AIProvider.DEEPSEEK.value:
                api_key = os.getenv('DEEPSEEK_API_KEY')
                if not api_key:
                    raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
                # Initialize OpenAI client with DeepSeek's base URL
                self.client = openai.OpenAI(
                    api_key=api_key,
                    base_url="https://api.deepseek.com/v1"
                )
                self.model = os.getenv('DEEPSEEK_MODEL', 'deepseek-chat')
                
            elif self.provider == AIProvider.OPENAI.value:
                api_key = os.getenv('OPENAI_API_KEY')
                if not api_key:
                    raise ValueError("OPENAI_API_KEY not found in environment variables")
                openai.api_key = api_key
                self.model = os.getenv('OPENAI_MODEL', 'gpt-4-turbo')
                
            elif self.provider == AIProvider.GOOGLE.value:
                api_key = os.getenv('GOOGLE_API_KEY')
                if not api_key:
                    raise ValueError("GOOGLE_API_KEY not found in environment variables")
                genai.configure(api_key=api_key)
                # Set default model and validate it
                self.model = os.getenv('GOOGLE_MODEL', 'gemini-1.5-pro')
                # Validate model name
                valid_google_models = ['gemini-2.5-flash-preview-04-17','gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-pro']
                if self.model not in valid_google_models:
                    logger.warning(f"Invalid Google model name: {self.model}. Using default 'gemini-1.5-pro'")
                    self.model = 'gemini-1.5-pro'
                
            elif self.provider == AIProvider.ANTHROPIC.value:
                api_key = os.getenv('ANTHROPIC_API_KEY')
                if not api_key:
                    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
                self.client = anthropic.Anthropic(api_key=api_key)
                self.model = os.getenv('ANTHROPIC_MODEL', 'claude-3-haiku-20240307')
                
            logger.info(f"Successfully initialized {self.provider} provider with model {self.model}")
                
        except Exception as e:
            logger.error(f"Error initializing AI provider: {str(e)}")
            raise

    def _scrape_page(self, url: str) -> Dict:
        """
        Scrape the content from a given URL, combining both page scraping and API content
        
        Args:
            url (str): The URL to scrape
            
        Returns:
            Dict: Scraped content
        """
        try:
            logger.info(f"Scraping URL: {url}")
            
            # Extract post type and slug from URL
            post_type, slug = self._extract_post_info_from_url(url)
            if not post_type or not slug:
                raise ValueError(f"Could not extract post type and slug from URL: {url}")
            
            # Get the correct endpoint from the mapping
            endpoint = ENDPOINT_MAP.get(post_type)
            if not endpoint:
                raise ValueError(f"Unsupported post type: {post_type}")
            
            # Initialize content data
            content_data = {
                'title': '',
                'content': '',
                'excerpt': '',
                'acf_fields': {},
                'url': url,
                'post_id': None,
                'feat_img_id': None,
                'post_type': post_type
            }
            
            # 1. Scrape the page content
            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract title
                title = soup.find('h1', class_='entry-title')
                if not title:
                    title = soup.find('title')
                content_data['title'] = title.text.strip() if title else ''
                
                # Extract main content - handle Elementor content
                content_div = soup.find('div', class_='elementor-widget-theme-post-content')
                if not content_div:
                    content_div = soup.find('div', class_='entry-content')
                if content_div:
                    # Remove unwanted elements
                    for element in content_div.find_all(['script', 'style', 'iframe', 'nav', 'footer', 'header']):
                        element.decompose()
                    content_data['content'] = content_div.get_text(separator=' ', strip=True)
                
                # Extract excerpt
                excerpt_div = soup.find('div', class_='elementor-widget-theme-post-excerpt')
                if not excerpt_div:
                    excerpt_div = soup.find('div', class_='entry-summary')
                if excerpt_div:
                    content_data['excerpt'] = excerpt_div.get_text(separator=' ', strip=True)
                    
            except Exception as e:
                logger.warning(f"Error scraping page content: {str(e)}")
            
            # 2. Get content from API
            try:
                api_url = f"{os.getenv('WORDPRESS_URL')}/wp-json/wp/v2/{endpoint}"
                response = requests.get(
                    api_url,
                    params={'slug': slug},
                    auth=(os.getenv('WORDPRESS_USERNAME'), os.getenv('WORDPRESS_PASSWORD'))
                )
                response.raise_for_status()
                
                posts = response.json()
                if posts:
                    post = posts[0]  # Get the first matching post
                    
                    # Store post ID and featured image ID
                    content_data['post_id'] = post.get('id')
                    content_data['feat_img_id'] = post.get('featured_media')
                    
                    # Update content from API if not found in page scraping
                    if not content_data['title']:
                        content_data['title'] = post.get('title', {}).get('rendered', '')
                    if not content_data['content']:
                        content_data['content'] = post.get('content', {}).get('rendered', '')
                    if not content_data['excerpt']:
                        content_data['excerpt'] = post.get('excerpt', {}).get('rendered', '')
                    
                    # Clean HTML from content
                    content_data['content'] = self._clean_html(content_data['content'])
                    content_data['excerpt'] = self._clean_html(content_data['excerpt'])
                    
                    # Extract ACF fields
                    for key, value in post.items():
                        if key.startswith('acf_'):
                            # Clean HTML from ACF fields
                            if isinstance(value, str):
                                value = self._clean_html(value)
                            content_data['acf_fields'][key] = value
                            
            except Exception as e:
                logger.warning(f"Error getting API content: {str(e)}")
            
            # Log extracted content
            logger.info("Extracted Content:")
            logger.info(f"Post ID: {content_data['post_id']}")
            logger.info(f"Featured Image ID: {content_data['feat_img_id']}")
            logger.info(f"Title: {content_data['title']}")
            logger.info(f"Content (first 200 chars): {content_data['content'][:200]}")
            logger.info(f"Excerpt: {content_data['excerpt']}")
            logger.info(f"ACF Fields: {list(content_data['acf_fields'].keys())}")
            
            return content_data
            
        except Exception as e:
            logger.error(f"Error scraping page {url}: {str(e)}")
            raise

    def _extract_post_info_from_url(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Extract post type and slug from URL
        
        Args:
            url (str): The URL to parse
            
        Returns:
            Tuple[Optional[str], Optional[str]]: (post_type, slug)
        """
        try:
            # Parse the URL
            parsed_url = urlparse(url)
            path_parts = [p for p in parsed_url.path.split('/') if p]
            
            # Get the slug (last part of the URL)
            slug = path_parts[-1] if path_parts else None
            
            # Check if this is a taxonomy page
            if len(path_parts) >= 2:
                # Check if the first part matches any of our endpoints
                for post_type, endpoint in ENDPOINT_MAP.items():
                    if path_parts[0] == endpoint:
                        return post_type, slug
                    # Special handling for service categories
                    elif post_type == 'stm_service' and path_parts[0] == 'categoria-servicio':
                        return 'stm_service_category', slug
            
            # If no match found and it's a root-level page (no specific post type in path)
            # then it's likely a page
            if len(path_parts) == 1:
                return 'page', slug
            
            # If no match found, try to determine from the content
            return None, slug
            
        except Exception as e:
            logger.error(f"Error extracting post info from URL {url}: {str(e)}")
            return None, None

    def _clean_html(self, html_content: str) -> str:
        """
        Clean HTML content to extract text
        
        Args:
            html_content (str): HTML content to clean
            
        Returns:
            str: Cleaned text content
        """
        if not html_content:
            return ''
            
        try:
            # Create a BeautifulSoup object
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Break into lines and remove leading and trailing space
            lines = (line.strip() for line in text.splitlines())
            # Break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # Drop blank lines
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text
            
        except Exception as e:
            logger.error(f"Error cleaning HTML content: {str(e)}")
            return html_content  # Return original content if cleaning fails

    def _detect_language(self, text: str) -> str:
        """
        Detect the language of the given text
        
        Args:
            text (str): Text to detect language from
            
        Returns:
            str: Detected language code (e.g., 'en', 'es')
        """
        try:
            if not text:
                return 'es'  # Default to Spanish if no text
            return langdetect.detect(text)
        except Exception as e:
            logger.warning(f"Language detection failed: {str(e)}")
            return 'es'  # Default to Spanish on error

    def _create_prompt(self, content: Dict, post_type: str) -> str:
        """
        Create a prompt for the AI model based on the content and post type
        
        Args:
            content (Dict): Dictionary containing page content
            post_type (str): The type of content being processed
            
        Returns:
            str: Formatted prompt for the AI model
        """
        # Get the context for this post type
        context = POST_TYPE_CONTEXT.get(post_type, {})
        
        # Detect language if not forced
        if not self.language:
            # Combine title and content for better language detection
            combined_text = f"{content.get('title', '')} {content.get('content', '')}"
            self.language = self._detect_language(combined_text)
        
        # Build the prompt based on post type and context
        prompt_parts = [
            f"Eres un consultor SEO experto especializado en {context.get('description', 'optimización de contenido')}.",
            f"Tu tarea es generar metadatos SEO optimizados para un {post_type} con el siguiente enfoque: {context.get('seo_focus', 'optimización general de contenido')}.",
            "Genera todos los metadatos en ESPAÑOL.",
            "\nDetalles del contenido:",
            f"Título: {content.get('title', '')}",
            f"Contenido: {content.get('content', '')[:self.config.max_content_length]}",  # Use config object
            f"Extracto: {content.get('excerpt', '')}",
        ]
        
        # Add specific instructions for blog posts
        if post_type == 'post':
            prompt_parts.extend([
                "\nEste es un artículo de blog. El contenido está renderizado con Elementor y puede contener HTML.",
                "El tema principal del artículo está indicado en el título y desarrollado en el contenido.",
                "Los metadatos deben reflejar el tema específico del artículo, no el concepto general de creación de contenido.",
                "Enfócate en:",
                "- El tema específico del artículo",
                "- Los puntos clave mencionados en el contenido",
                "- El valor que aporta al lector",
                "- La relevancia para el público objetivo"
            ])
        
        # Add ACF fields if present
        if 'acf_fields' in content and content['acf_fields']:
            prompt_parts.append("\nCampos adicionales:")
            for field, value in content['acf_fields'].items():
                prompt_parts.append(f"{field}: {value}")
        
        # Add specific instructions based on post type
        if post_type == 'stm_service_category':
            prompt_parts.extend([
                "\nComo esta es una página de categoría de servicio, enfócate en:",
                "- Crear una descripción general completa de la categoría de servicio",
                "- Destacar los principales beneficios y características de los servicios en esta categoría",
                "- Usar terminología específica de la categoría y términos de la industria",
                "- Enfatizar la experiencia y especialización en esta área de servicio"
            ])
        elif post_type == 'stm_service':
            prompt_parts.extend([
                "\nComo esta es una página de servicio, enfócate en:",
                "- Destacar la propuesta de valor única del servicio",
                "- Enfatizar los beneficios y resultados para los clientes",
                "- Usar un lenguaje claro y orientado a la acción",
                "- Incluir términos relevantes de la industria e indicadores de experiencia"
            ])
        elif post_type == 'stm_staff':
            prompt_parts.extend([
                "\nComo esta es una página de perfil de personal, enfócate en:",
                "- Destacar la experiencia profesional y calificaciones",
                "- Enfatizar habilidades y experiencia únicas",
                "- Crear una conexión personal con clientes potenciales",
                "- Generar confianza y credibilidad"
            ])
        
        # Add metadata requirements
        prompt_parts.extend([
            "\nPor favor, genera los siguientes metadatos SEO en este formato exacto:",
            "Meta Título: [Tu meta título aquí, máximo 60 caracteres]",
            "Meta Descripción: [Tu meta descripción aquí, máximo 160 caracteres]",
            "Palabra Clave Principal: [Tu palabra clave principal aquí]",
            "Título Open Graph: [Tu título OG aquí]",
            "Descripción Open Graph: [Tu descripción OG aquí]",
            "Título Twitter Card: [Tu título de Twitter aquí]",
            "Descripción Twitter Card: [Tu descripción de Twitter aquí]",
            "\nImportante:",
            "- Cada campo debe comenzar con su nombre exacto seguido de dos puntos",
            "- No incluyas texto adicional antes o después de los campos de metadatos",
            "- Mantén cada campo en una sola línea",
            "- Asegúrate de que todos los metadatos:",
            "  * Estén optimizados para el tipo de contenido y enfoque especificados",
            "  * Sigan las mejores prácticas de SEO",
            "  * Sean atractivos y generen clics",
            "  * Mantengan la voz de la marca y la consistencia",
            "  * Reflejen el tema específico del artículo"
        ])
        
        return "\n".join(prompt_parts)

    def _parse_metadata_response(self, response_text: str, content: Dict) -> Dict:
        """
        Parse the AI response into structured metadata
        
        Args:
            response_text (str): Raw response from AI model
            content (Dict): Original content for reference
            
        Returns:
            Dict: Structured metadata
        """
        metadata = {
            'meta_title': '',
            'meta_description': '',
            'focus_keyword': '',
            'canonical_url': content['url'],
            'og_title': '',
            'og_description': '',
            'twitter_title': '',
            'twitter_description': '',
            'language': self.language,
            'post_id': content.get('post_id'),
            'feat_img_id': content.get('feat_img_id')
        }
        
        # Split the response into lines and clean them
        lines = [line.strip() for line in response_text.split('\n') if line.strip()]
        
        # Define field mappings with variations in both English and Spanish
        field_mappings = {
            'meta_title': ['meta title', 'title', 'meta-title', 'meta título', 'título meta'],
            'meta_description': ['meta description', 'description', 'meta-description', 'meta descripción', 'descripción meta'],
            'focus_keyword': ['focus keyword', 'keyword', 'primary keyword', 'palabra clave principal', 'palabra clave'],
            'og_title': ['open graph title', 'og title', 'og-title', 'título open graph', 'título og'],
            'og_description': ['open graph description', 'og description', 'og-description', 'descripción open graph', 'descripción og'],
            'twitter_title': ['twitter card title', 'twitter title', 'twitter-title', 'título twitter card', 'título twitter'],
            'twitter_description': ['twitter card description', 'twitter description', 'twitter-description', 'descripción twitter card', 'descripción twitter']
        }
        
        current_field = None
        current_value = []
        
        for line in lines:
            # Check if this line starts a new field
            for field, variations in field_mappings.items():
                if any(line.lower().startswith(variation.lower() + ':') for variation in variations):
                    # If we were collecting a previous field, save it
                    if current_field and current_value:
                        metadata[current_field] = ' '.join(current_value).strip()
                    
                    # Start collecting the new field
                    current_field = field
                    # Extract the value after the colon
                    value = line.split(':', 1)[1].strip() if ':' in line else ''
                    current_value = [value]
                    break
            else:
                # If we're in the middle of collecting a field value, add this line
                if current_field:
                    current_value.append(line)
        
        # Save the last field if we were collecting one
        if current_field and current_value:
            metadata[current_field] = ' '.join(current_value).strip()
        
        # Add region to focus keyword and meta description if region is specified
        if self.region_config and self.region_config.region != 'global':
            region = self.region_config.region
            # Add region to focus keyword
            if metadata['focus_keyword']:
                metadata['focus_keyword'] = f"{metadata['focus_keyword']} {region}"
            
            # Add region to meta description if not already present
            if metadata['meta_description'] and region.lower() not in metadata['meta_description'].lower():
                # Try to add region before the call-to-action if present
                if '¡Contáctanos!' in metadata['meta_description']:
                    metadata['meta_description'] = metadata['meta_description'].replace(
                        '¡Contáctanos!', 
                        f'en {region} ¡Contáctanos!'
                    )
                else:
                    # Add region at the end if no call-to-action
                    metadata['meta_description'] = f"{metadata['meta_description']} en {region}"
        
        # Ensure proper character encoding for Spanish characters
        for field in metadata:
            if isinstance(metadata[field], str):
                # First decode any Unicode escape sequences
                try:
                    metadata[field] = metadata[field].encode('latin1').decode('unicode-escape')
                except:
                    pass
                # Then ensure proper UTF-8 encoding
                try:
                    metadata[field] = metadata[field].encode('utf-8').decode('utf-8')
                except:
                    pass
        
        # Log the parsed metadata for debugging
        logger.debug("Parsed Metadata:")
        for key, value in metadata.items():
            logger.debug(f"{key}: {value}")
        
        return metadata

    def _generate_with_openai(self, prompt: str) -> Tuple[str, int, int]:
        """Generate response using OpenAI"""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert SEO consultant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        self.last_input_tokens = response.usage.prompt_tokens
        self.last_output_tokens = response.usage.completion_tokens
        self.last_total_tokens = response.usage.total_tokens
        return (
            response.choices[0].message.content,
            self.last_input_tokens,
            self.last_output_tokens
        )

    def _generate_with_google(self, prompt: str) -> Tuple[str, int, int]:
        """Generate response using Google Gemini"""
        try:
            # Configure generation parameters
            generation_config = {
                "temperature": 0.7,
                "top_p": 0.8,
                "top_k": 40,
                "max_output_tokens": 500,
            }
            
            # Initialize model with proper configuration
            model = genai.GenerativeModel(
                model_name=self.model,
                generation_config=generation_config
            )
            
            # Generate content with retries
            max_retries = 3
            delay = 2.0  # Base delay in seconds
            
            for attempt in range(max_retries + 1):
                try:
                    # Create the chat session
                    chat = model.start_chat()
                    
                    # Send the message
                    response = chat.send_message(prompt)
                    
                    # Check for blocked content
                    if not response.candidates:
                        logger.error(f"Response blocked/empty: {response.prompt_feedback}")
                        if attempt < max_retries:
                            sleep(delay * (2 ** attempt))
                            continue
                        return "", 0, 0
                    
                    # Calculate approximate token counts
                    self.last_input_tokens = len(prompt) // 4  # Approximate tokens
                    self.last_output_tokens = len(response.text) // 4  # Approximate tokens
                    self.last_total_tokens = self.last_input_tokens + self.last_output_tokens
                    
                    return response.text, self.last_input_tokens, self.last_output_tokens
                    
                except Exception as e:
                    if attempt < max_retries:
                        wait = delay * (2 ** attempt)
                        logger.warning(f"Google API error ({type(e).__name__}). Retrying in {wait:.1f}s...")
                        sleep(wait)
                    else:
                        logger.error(f"Google API error after {max_retries} retries: {str(e)}")
                        raise
                        
        except Exception as e:
            logger.error(f"Error generating with Google: {str(e)}")
            raise

    def _generate_with_deepseek(self, prompt: str) -> Tuple[str, int, int]:
        """Generate response using DeepSeek"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert SEO consultant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            self.last_input_tokens = response.usage.prompt_tokens
            self.last_output_tokens = response.usage.completion_tokens
            self.last_total_tokens = response.usage.total_tokens
            return (
                response.choices[0].message.content,
                self.last_input_tokens,
                self.last_output_tokens
            )
        except Exception as e:
            logger.error(f"Error generating with DeepSeek: {str(e)}")
            raise

    def _generate_with_anthropic(self, prompt: str) -> Tuple[str, int, int]:
        """Generate response using Anthropic Claude"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=500,
            temperature=0.7,
            system="You are an expert SEO consultant.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        self.last_input_tokens = response.usage.input_tokens
        self.last_output_tokens = response.usage.output_tokens
        self.last_total_tokens = self.last_input_tokens + self.last_output_tokens
        return (
            response.content[0].text,
            self.last_input_tokens,
            self.last_output_tokens
        )

    def generate_metadata(self, page_url: str, post_type: str) -> Optional[Dict]:
        """
        Generate SEO metadata for a given URL.
        
        Args:
            page_url (str): The URL to generate metadata for
            post_type (str): The type of post (e.g., 'post', 'page', etc.)
            
        Returns:
            Optional[Dict]: Generated metadata or None if error
        """
        try:
            # Scrape the page content
            content = self._scrape_page(page_url)
            if not content:
                logger.error(f"Failed to scrape content from {page_url}")
                return None
                
            # Create the prompt
            prompt = self._create_prompt(content, post_type)
            
            # Generate metadata using the selected provider
            if self.provider == AIProvider.OPENAI.value:
                response_text, input_tokens, output_tokens = self._generate_with_openai(prompt)
            elif self.provider == AIProvider.GOOGLE.value:
                response_text, input_tokens, output_tokens = self._generate_with_google(prompt)
            elif self.provider == AIProvider.DEEPSEEK.value:
                response_text, input_tokens, output_tokens = self._generate_with_deepseek(prompt)
            elif self.provider == AIProvider.ANTHROPIC.value:
                response_text, input_tokens, output_tokens = self._generate_with_anthropic(prompt)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
                
            # Parse the response
            metadata = self._parse_metadata_response(response_text, content)
            
            # Calculate cost
            cost = self.cost_calculator.calculate_cost(
                provider=self.provider,
                model=self.model,
                input_tokens=input_tokens,
                output_tokens=output_tokens
            )
            
            # Add processing info
            metadata['processing_info'] = {
                'provider': self.provider,
                'model': self.model,
                'timestamp': datetime.now().isoformat(),
                'cost': cost,
                'input_tokens': input_tokens,
                'output_tokens': output_tokens,
                'total_tokens': input_tokens + output_tokens
            }
            
            # Add post ID and featured image ID
            metadata['post_id'] = content['post_id']
            metadata['feat_img_id'] = content['feat_img_id']
            
            return metadata
            
        except Exception as e:
            logger.error(f"Error generating metadata for {page_url}: {str(e)}")
            return None

    def get_cost_summary(self) -> str:
        """
        Get a summary of API usage and costs
        
        Returns:
            str: Formatted cost summary
        """
        return self.cost_calculator.get_usage_summary()

    def process_taxonomies(self, taxonomy_name: str, terms: Optional[List[str]] = None) -> Dict[str, List[Dict]]:
        """
        Process taxonomy terms and generate metadata for each term.
        
        Args:
            taxonomy_name (str): Name of the taxonomy to process
            terms (Optional[List[str]]): Optional list of specific terms to process
            
        Returns:
            Dict[str, List[Dict]]: Dictionary mapping taxonomy names to generated metadata
        """
        try:
            # Initialize results structure
            results = {taxonomy_name: []}
            
            # Get the correct endpoint for the taxonomy
            endpoint = ENDPOINT_MAP.get(taxonomy_name)
            if not endpoint:
                raise ValueError(f"Unsupported taxonomy: {taxonomy_name}")
            
            # Build the API URL
            api_url = f"{os.getenv('WORDPRESS_URL')}/wp-json/wp/v2/{endpoint}"
            
            # Get terms from API
            response = requests.get(
                api_url,
                auth=(os.getenv('WORDPRESS_USERNAME'), os.getenv('WORDPRESS_PASSWORD'))
            )
            response.raise_for_status()
            
            # Filter terms if specific terms are requested
            all_terms = response.json()
            if terms:
                all_terms = [term for term in all_terms if term.get('slug') in terms]
            
            # Process each term
            for term in tqdm(all_terms, desc=f"Processing {taxonomy_name} terms"):
                try:
                    # Extract term content
                    content = {
                        'title': term.get('name', ''),
                        'content': term.get('description', ''),
                        'excerpt': term.get('description', ''),
                        'url': term.get('link', '')
                    }
                    
                    # Create prompt for the term
                    prompt = self._create_prompt(content, taxonomy_name)
                    
                    # Generate metadata
                    response_text, input_tokens, output_tokens = self._generate_with_google(prompt)
                    
                    # Parse the response into structured metadata
                    metadata = self._parse_metadata_response(response_text, content)
                    
                    if metadata:
                        results[taxonomy_name].append({
                            'term': term.get('name', ''),
                            'slug': term.get('slug', ''),
                            'url': term.get('link', ''),
                            'metadata': metadata
                        })
                        
                except Exception as e:
                    logger.error(f"Error processing term {term.get('name', '')}: {e}")
                    
            return results
            
        except Exception as e:
            logger.error(f"Error processing taxonomy {taxonomy_name}: {e}")
            return {}

    def generate_metadata_for_post(self, content: str, title: str, excerpt: str) -> Dict[str, Any]:
        """
        Generate SEO metadata for a post
        
        Args:
            content (str): Post content
            title (str): Post title
            excerpt (str): Post excerpt
            
        Returns:
            Dict[str, Any]: Generated metadata
        """
        try:
            # Clean and prepare content
            cleaned_content = self._clean_content(content)
            cleaned_title = self._clean_text(title)
            cleaned_excerpt = self._clean_text(excerpt)

            # Generate focus keywords first
            focus_keywords = self._generate_focus_keywords(cleaned_content, cleaned_title)
            primary_keyword = focus_keywords[0] if focus_keywords else ""

            # Generate optimized metadata ensuring focus keyword presence
            metadata = {
                'title': self._generate_title(cleaned_title, primary_keyword),
                'description': self._generate_description(cleaned_excerpt, cleaned_content, primary_keyword),
                'focus_keyword': primary_keyword,
                'secondary_keywords': focus_keywords[1:],
                'keyword_density': self._calculate_keyword_density(cleaned_content, primary_keyword)
            }

            # Add region suffix if not global
            if self.config.region != 'global':
                metadata['title'] = self._add_region_suffix(metadata['title'])
                metadata['focus_keyword'] = f"{metadata['focus_keyword']} {self.config.region}"

            # Validate metadata
            self._validate_metadata(metadata)

            return metadata

        except Exception as e:
            logger.error(f"Error generating metadata: {str(e)}")
            raise

    def _clean_content(self, content: str) -> str:
        """Clean and prepare content for processing"""
        # Remove HTML tags
        content = re.sub(r'<[^>]+>', ' ', content)
        # Remove extra whitespace
        content = re.sub(r'\s+', ' ', content)
        # Remove special characters but keep spaces
        content = re.sub(r'[^\w\s]', ' ', content)
        return content.strip().lower()

    def _clean_text(self, text: str) -> str:
        """Clean text for title and description"""
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def _generate_focus_keywords(self, content: str, title: str) -> List[str]:
        """Generate focus keywords ensuring no repetition"""
        # Combine title and content for keyword extraction
        text = f"{title} {content}"
        words = text.split()
        word_freq = {}
        
        # Count word frequency
        for word in words:
            if len(word) >= self.keyword_min_length and word not in self.used_keywords:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Sort by frequency
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        keywords = []
        
        # Get top keywords avoiding repetition
        for word, _ in sorted_words:
            if len(keywords) < self.keyword_recommended_count and word not in self.used_keywords:
                keywords.append(word)
                self.used_keywords.add(word)
        
        return keywords

    def _calculate_keyword_density(self, content: str, keyword: str) -> float:
        """Calculate keyword density in content"""
        if not keyword or not content:
            return 0.0
            
        total_words = len(content.split())
        keyword_count = len(re.findall(rf'\b{re.escape(keyword)}\b', content))
        
        if total_words == 0:
            return 0.0
            
        return round((keyword_count / total_words) * 100, 2)

    def _generate_title(self, title: str, focus_keyword: str) -> str:
        """Generate optimized title ensuring focus keyword presence"""
        # Ensure focus keyword is in title
        if focus_keyword and focus_keyword.lower() not in title.lower():
            # Try to add focus keyword at the beginning
            if len(f"{focus_keyword}: {title}") <= self.title_max_length:
                return f"{focus_keyword}: {title}"
            # If too long, try to truncate title to make room
            max_title_length = self.title_max_length - len(focus_keyword) - 2
            if max_title_length > 0:
                truncated_title = title[:max_title_length-3]
                return f"{focus_keyword}: {truncated_title}"
        
        # If focus keyword is already in title or we can't add it, just truncate if needed
        if len(title) > self.title_max_length:
            return title[:self.title_max_length-3] + "..."
        
        return title

    def _generate_description(self, excerpt: str, content: str, focus_keyword: str) -> str:
        """Generate optimized description ensuring focus keyword presence"""
        # Start with excerpt if available, otherwise use first sentence of content
        description = excerpt if excerpt else (re.split(r'[.!?]', content)[0] if content else "")
        
        # Ensure focus keyword is in description
        if focus_keyword and focus_keyword.lower() not in description.lower():
            # Try to add focus keyword at the beginning
            if len(f"{focus_keyword} - {description}") <= self.description_max_length:
                return f"{focus_keyword} - {description}"
            # If too long, truncate description to make room
            max_desc_length = self.description_max_length - len(focus_keyword) - 3
            if max_desc_length > 0:
                truncated_desc = description[:max_desc_length-3] + "..."
                return f"{focus_keyword} - {truncated_desc}"
        
        # If focus keyword is already in description or we can't add it, just truncate if needed
        if len(description) > self.description_max_length:
            return description[:self.description_max_length-3] + "..."
        
        return description

    def _add_region_suffix(self, title: str) -> str:
        """Add region suffix to title"""
        suffix = f" - {self.config.region}"
        if len(title) + len(suffix) <= self.title_max_length:
            return title + suffix
        else:
            max_title_length = self.title_max_length - len(suffix)
            return title[:max_title_length-3] + "..." + suffix

    def _validate_metadata(self, metadata: Dict[str, Any]) -> None:
        """Validate generated metadata"""
        # Validate title
        if not metadata['title']:
            raise ValueError("Title cannot be empty")
        if len(metadata['title']) > self.title_absolute_max:
            raise ValueError(f"Title exceeds maximum length of {self.title_absolute_max} characters")
        if metadata['focus_keyword'] and metadata['focus_keyword'].lower() not in metadata['title'].lower():
            raise ValueError("Focus keyword must appear in title")
            
        # Validate description
        if not metadata['description']:
            raise ValueError("Description cannot be empty")
        if len(metadata['description']) > self.description_absolute_max:
            raise ValueError(f"Description exceeds maximum length of {self.description_absolute_max} characters")
        if metadata['focus_keyword'] and metadata['focus_keyword'].lower() not in metadata['description'].lower():
            raise ValueError("Focus keyword must appear in description")
            
        # Validate keyword density
        if metadata['keyword_density'] == 0.0:
            logger.warning("Keyword density is 0.0%, consider increasing focus keyword usage in content")
        elif metadata['keyword_density'] > 3.0:
            logger.warning("Keyword density is above 3%, consider reducing focus keyword usage to avoid keyword stuffing")

    def generate_title(self, content: str, keywords: list[str], brand_name: str = None) -> str:
        """
        Generate an SEO-optimized title based on content and keywords.
        
        Args:
            content: The main content to generate title from
            keywords: Target keywords to include
            brand_name: Optional brand name to append
            
        Returns:
            An optimized title string
        """
        try:
            # Extract main topic/subject from content
            main_topic = self._extract_main_topic(content)
            
            # Get primary keyword (first in list)
            primary_keyword = keywords[0] if keywords else ""
            
            # Build title components
            title_parts = []
            
            # Add primary keyword near start if relevant
            if primary_keyword and primary_keyword.lower() not in main_topic.lower():
                title_parts.append(primary_keyword)
            
            # Add main topic
            title_parts.append(main_topic)
            
            # Add value proposition or power word if appropriate
            value_prop = self._get_value_proposition(content)
            if value_prop:
                title_parts.append(value_prop)
                
            # Join parts with appropriate separators
            title = " - ".join(filter(None, title_parts))
            
            # Append brand if provided
            if brand_name:
                # Ensure title + brand fits in ~60 chars
                max_title_len = 60 - len(brand_name) - 3
                if len(title) > max_title_len:
                    title = title[:max_title_len].rstrip()
                title = f"{title} | {brand_name}"
            
            # Truncate to 60 chars if needed
            if len(title) > 60:
                title = title[:57].rstrip() + "..."
                
            return title
            
        except Exception as e:
            self.logger.error(f"Error generating title: {str(e)}")
            return ""
            
    def _extract_main_topic(self, content: str) -> str:
        """
        Extract the main topic from content using NLP.
        Uses noun phrase extraction and named entity recognition.
        """
        try:
            if not self.nlp:
                return content[:50]  # Fallback if NLP not available
                
            # Process content with spaCy
            doc = self.nlp(content[:1000])  # Process first 1000 chars for efficiency
            
            # Extract noun phrases
            noun_phrases = [chunk.text for chunk in doc.noun_chunks]
            
            # Get named entities
            entities = [ent.text for ent in doc.ents]
            
            # Combine and count occurrences
            topics = noun_phrases + entities
            topic_counts = Counter(topics)
            
            # Get most common meaningful topic
            for topic, _ in topic_counts.most_common(5):
                # Skip very short or very long topics
                if 3 <= len(topic) <= 40:
                    return topic
                    
            return content[:50]  # Fallback to first 50 chars
            
        except Exception as e:
            self.logger.error(f"Error extracting main topic: {str(e)}")
            return content[:50]

    def _get_value_proposition(self, content: str) -> str:
        """
        Get relevant value proposition or power word based on content sentiment
        and common marketing phrases.
        """
        try:
            # Analyze sentiment
            blob = TextBlob(content)
            sentiment = blob.sentiment.polarity
            
            # Define power words based on sentiment
            positive_words = [
                "Ultimate", "Complete", "Essential", "Proven",
                "Comprehensive", "Expert", "Professional"
            ]
            neutral_words = [
                "Guide", "Tutorial", "Overview", "Analysis",
                "Review", "Comparison"
            ]
            negative_words = [
                "Solution", "Fix", "Resolve", "Prevent",
                "Avoid", "Overcome"
            ]
            
            # Select appropriate power word based on sentiment
            if sentiment > 0.2:
                return positive_words[hash(content) % len(positive_words)]
            elif sentiment < -0.2:
                return negative_words[hash(content) % len(negative_words)]
            else:
                return neutral_words[hash(content) % len(neutral_words)]
                
        except Exception as e:
            self.logger.error(f"Error getting value proposition: {str(e)}")
            return ""

    def generate_description(self, content: str, keywords: list[str]) -> str:
        """
        Generate an SEO-optimized meta description.
        
        Args:
            content: The main content to generate description from
            keywords: Target keywords to include
            
        Returns:
            An optimized meta description string
        """
        try:
            # Extract key points from content
            key_points = self._extract_key_points(content)
            
            # Build compelling description incorporating keywords naturally
            description = self._build_description(key_points, keywords)
            
            # Add call-to-action if appropriate
            cta = self._get_cta(content)
            if cta:
                description = f"{description} {cta}"
                
            # Ensure description is under 160 chars
            if len(description) > 160:
                description = description[:157].rstrip() + "..."
                
            return description
            
        except Exception as e:
            self.logger.error(f"Error generating description: {str(e)}")
            return ""
            
    def _extract_key_points(self, content: str, max_points: int = 3) -> list[str]:
        """
        Extract key points from content using NLP techniques.
        Returns a list of the most important sentences.
        """
        try:
            if not self.nlp:
                return [content[:100]]  # Fallback if NLP not available
                
            # Process content with spaCy
            doc = self.nlp(content[:2000])  # Process first 2000 chars for efficiency
            
            # Score sentences based on important features
            sentence_scores = {}
            for sent in doc.sents:
                # Skip very short sentences
                if len(sent.text.split()) < 4:
                    continue
                    
                score = 0
                # Score based on named entities
                score += len([ent for ent in sent.ents])
                # Score based on noun phrases
                score += len([chunk for chunk in sent.noun_chunks])
                # Score based on position (earlier sentences more important)
                score += 1.0 / (1 + sent.start)
                
                sentence_scores[sent.text] = score
            
            # Get top scoring sentences
            top_sentences = sorted(
                sentence_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )[:max_points]
            
            return [sent for sent, _ in top_sentences]
            
        except Exception as e:
            self.logger.error(f"Error extracting key points: {str(e)}")
            return [content[:100]]

    def _build_description(self, key_points: list[str], max_length: int = 155) -> str:
        """
        Build a compelling meta description from key points.
        Ensures the description is within character limits.
        """
        try:
            # Start with first key point
            if not key_points:
                return ""
                
            description = key_points[0]
            current_length = len(description)
            
            # Add additional points if space allows
            for point in key_points[1:]:
                # Account for spacing and ellipsis
                if current_length + len(point) + 5 > max_length:
                    break
                    
                description += f". {point}"
                current_length = len(description)
            
            # Truncate if still too long
            if len(description) > max_length:
                description = description[:max_length-3] + "..."
                
            return description
            
        except Exception as e:
            self.logger.error(f"Error building description: {str(e)}")
            return key_points[0][:155] if key_points else ""

    def _get_cta(self, content_type: str) -> str:
        """
        Get an appropriate call-to-action based on content type.
        """
        try:
            cta_map = {
                "article": "Learn more",
                "product": "Shop now",
                "service": "Get started",
                "guide": "Read the guide",
                "tutorial": "Start learning",
                "review": "Read our review",
                "comparison": "Compare now",
                "news": "Read full story"
            }
            
            # Default to generic CTA if type not found
            return cta_map.get(content_type.lower(), "Learn more")
            
        except Exception as e:
            self.logger.error(f"Error getting CTA: {str(e)}")
            return "Learn more" 