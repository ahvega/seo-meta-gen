"""
Cost calculator for AI API usage
"""

from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class CostCalculator:
    # Latest API prices (as of April 2024)
    PRICES = {
        'anthropic': {
            'claude-3-haiku-20240307': {
                'input': 0.25 / 1_000_000,  # $0.25 per million tokens
                'output': 1.25 / 1_000_000,  # $1.25 per million tokens
            },
            'claude-3-sonnet-20240229': {
                'input': 3.00 / 1_000_000,  # $3.00 per million tokens
                'output': 15.00 / 1_000_000,  # $15.00 per million tokens
            },
            'claude-3-opus-20240229': {
                'input': 15.00 / 1_000_000,  # $15.00 per million tokens
                'output': 75.00 / 1_000_000,  # $75.00 per million tokens
            }
        },
        'openai': {
            'gpt-3.5-turbo': {
                'input': 0.50 / 1_000_000,  # $0.50 per million tokens
                'output': 1.50 / 1_000_000,  # $1.50 per million tokens
            },
            'gpt-4': {
                'input': 30.00 / 1_000_000,  # $30.00 per million tokens
                'output': 60.00 / 1_000_000,  # $60.00 per million tokens
            },
            'gpt-4-turbo': {
                'input': 10.00 / 1_000_000,  # $10.00 per million tokens
                'output': 30.00 / 1_000_000,  # $30.00 per million tokens
            }
        },
        'google': {
            'gemini-1.5-pro': {
                'input': 0.25 / 1_000_000,  # $0.25 per million tokens
                'output': 0.50 / 1_000_000,  # $0.50 per million tokens
            },
            'gemini-1.5-flash': {
                'input': 0.10 / 1_000_000,  # $0.10 per million tokens
                'output': 0.30 / 1_000_000,  # $0.30 per million tokens
            },
            'gemini-pro': {
                'input': 0.25 / 1_000_000,  # $0.25 per million tokens
                'output': 0.50 / 1_000_000,  # $0.50 per million tokens
            },
            'gemini-2.5-flash-preview-04-17': {
                'input': 0.15 / 1_000_000,  # $0.15 per million tokens
                'output': 0.45 / 1_000_000,  # $0.45 per million tokens
            }
        },
        'deepseek': {
            'deepseek-chat': {
                'input': 0.10 / 1_000_000,  # $0.10 per million tokens
                'output': 0.20 / 1_000_000,  # $0.20 per million tokens
            }
        }
    }

    def __init__(self):
        self.total_cost = 0.0
        self.usage_details: Dict[str, Dict[str, int]] = {}

    def calculate_cost(self, provider: str, model: str, input_tokens: int, output_tokens: int) -> float:
        """
        Calculate the cost for a specific API call
        
        Args:
            provider (str): The AI provider (anthropic, openai, google, deepseek)
            model (str): The model name
            input_tokens (int): Number of input tokens
            output_tokens (int): Number of output tokens
            
        Returns:
            float: The calculated cost in USD
        """
        try:
            prices = self.PRICES.get(provider, {}).get(model)
            if not prices:
                logger.warning(f"No pricing information found for {provider}/{model}")
                return 0.0

            input_cost = input_tokens * prices['input']
            output_cost = output_tokens * prices['output']
            total_cost = input_cost + output_cost

            # Store usage details
            if provider not in self.usage_details:
                self.usage_details[provider] = {}
            if model not in self.usage_details[provider]:
                self.usage_details[provider][model] = {
                    'input_tokens': 0,
                    'output_tokens': 0,
                    'cost': 0.0
                }

            self.usage_details[provider][model]['input_tokens'] += input_tokens
            self.usage_details[provider][model]['output_tokens'] += output_tokens
            self.usage_details[provider][model]['cost'] += total_cost

            self.total_cost += total_cost
            return total_cost

        except Exception as e:
            logger.error(f"Error calculating cost: {str(e)}")
            return 0.0

    def get_usage_summary(self) -> str:
        """
        Get a formatted summary of API usage and costs
        
        Returns:
            str: Formatted usage summary
        """
        summary = ["API Usage Summary:"]
        for provider, models in self.usage_details.items():
            summary.append(f"\n{provider.upper()}:")
            for model, usage in models.items():
                summary.append(f"  {model}:")
                summary.append(f"    Input tokens: {usage['input_tokens']:,}")
                summary.append(f"    Output tokens: {usage['output_tokens']:,}")
                summary.append(f"    Cost: ${usage['cost']:.6f}")
        
        summary.append(f"\nTotal Cost: ${self.total_cost:.6f}")
        return "\n".join(summary) 