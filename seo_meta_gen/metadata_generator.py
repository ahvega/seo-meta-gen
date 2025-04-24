"""
AI-driven SEO metadata generation module with multi-provider support
"""

import os
from typing import Dict, Optional, Tuple, List
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
from .config import ENDPOINT_MAP, POST_TYPE_CONTEXT, DEFAULT_CONFIG
from urllib.parse import urlparse
from time import sleep
import langdetect
from langdetect import DetectorFactory
import json
from datetime import datetime

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
    
    def __init__(self, provider: Optional[str] = None, language: Optional[str] = None):
        """Initialize the MetadataGenerator."""
        self.current_provider = None
        self.current_model = None
        self.last_cost = 0.0
        self.last_input_tokens = 0
        self.last_output_tokens = 0
        self.last_total_tokens = 0
        self.provider = provider or os.getenv('PREFERRED_AI_PROVIDER', 'google')
        self.model = None
        self.cost_calculator = CostCalculator()
        self.language = language  # Store the forced language if provided
        logger.debug(f"Initializing MetadataGenerator with provider: {self.provider}")
        self._initialize_provider()

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
                valid_google_models = ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-pro']
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
                'post_type': post_type,
                'processing_info': {
                    'provider': self.provider,
                    'model': self.model,
                    'timestamp': None,
                    'cost': None
                }
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
                    
                    # Store post ID
                    content_data['post_id'] = post.get('id')
                    
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
            f"Contenido: {content.get('content', '')[:DEFAULT_CONFIG['max_content_length']]}",
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
            'language': self.language
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
            
            # Update processing info
            content['processing_info'].update({
                'timestamp': datetime.now().isoformat(),
                'cost': cost,
                'input_tokens': input_tokens,
                'output_tokens': output_tokens,
                'total_tokens': input_tokens + output_tokens
            })
            
            # Add processing info to metadata
            metadata['processing_info'] = content['processing_info']
            
            # Add post ID to metadata
            metadata['post_id'] = content['post_id']
            
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