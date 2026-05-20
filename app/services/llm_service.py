"""LLM integration service for narrative generation."""

import logging
from typing import Optional
from openai import OpenAI, APIError

from app.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


class LLMService:
    """Service for LLM interactions."""

    def __init__(self):
        """Initialize LLM service with OpenAI client."""
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
        self.temperature = settings.openai_temperature
        self.max_tokens = settings.openai_max_tokens

    async def generate_narrative(
        self, prompt: str, system_message: Optional[str] = None
    ) -> str:
        """Generate narrative using LLM.

        Args:
            prompt: The user prompt for narrative generation
            system_message: Optional system message for context

        Returns:
            Generated narrative text

        Raises:
            APIError: If LLM API call fails
        """
        try:
            messages = []

            if system_message:
                messages.append({"role": "system", "content": system_message})

            messages.append({"role": "user", "content": prompt})

            logger.info(f"Calling {self.model} with prompt of length {len(prompt)}")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )

            narrative = response.choices[0].message.content
            logger.info(f"Generated narrative of length {len(narrative)}")

            return narrative

        except APIError as e:
            logger.error(f"LLM API error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in LLM generation: {str(e)}")
            raise
