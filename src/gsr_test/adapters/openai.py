"""OpenAI adapter implementation."""

import time
from typing import AsyncIterator
from openai import AsyncOpenAI
import tiktoken
from datetime import datetime

from gsr_test.core.adapter import ModelAdapter
from gsr_test.core.response import Response, ModelInfo


class OpenAIAdapter(ModelAdapter):
    """Adapter for OpenAI models (GPT-4, GPT-3.5, etc.)."""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        """Initialize the OpenAI adapter.
        
        Args:
            api_key: Your OpenAI API key
            model: Model name (e.g., "gpt-4", "gpt-4-turbo", "gpt-3.5-turbo")
        """
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model
        
        # Get the appropriate tokenizer for this model
        try:
            self.encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            # If tiktoken doesn't recognize the model, use the standard encoding
            # cl100k_base is used by gpt-4, gpt-3.5-turbo, and text-embedding-ada-002
            self.encoding = tiktoken.get_encoding("cl100k_base")
    
    async def generate(self, prompt: str, **kwargs) -> Response:
        """Generate a response using OpenAI's API.
        
        Args:
            prompt: The input prompt
            **kwargs: Optional parameters like temperature, max_tokens, etc.
            
        Returns:
            Standardized Response object
        """
        start = time.time()
        
        # Call OpenAI API
        result = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        
        # Calculate latency in milliseconds
        latency = (time.time() - start) * 1000
        
        # Convert OpenAI's response to our standard format
        return Response(
            content=result.choices[0].message.content or "",
            model=result.model,
            prompt_tokens=result.usage.prompt_tokens,
            completion_tokens=result.usage.completion_tokens,
            total_tokens=result.usage.total_tokens,
            finish_reason=result.choices[0].finish_reason,
            latency_ms=latency,
            timestamp=datetime.now(),
            metadata={
                "system_fingerprint": result.system_fingerprint,
            },
            raw_response=result
        )
    
    async def generate_stream(self, prompt: str, **kwargs) -> AsyncIterator[str]:
        """Generate a streaming response from OpenAI.
        
        Args:
            prompt: The input prompt
            **kwargs: Optional parameters
            
        Yields:
            Text chunks as they arrive
        """
        stream = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            **kwargs
        )
        
        async for chunk in stream:
            # Check if this chunk has content
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    def count_tokens(self, text: str) -> int:
        """Count tokens using tiktoken.
        
        Args:
            text: Text to count
            
        Returns:
            Number of tokens
        """
        return len(self.encoding.encode(text))
    
    def get_model_info(self) -> ModelInfo:
        """Get information about the OpenAI model.
        
        Returns:
            ModelInfo with model capabilities and costs
        """
        # Model configurations based on OpenAI's documentation
        configs = {
            "gpt-4": {
                "context": 8192,
                "max_out": 4096,
                "in_cost": 0.03,
                "out_cost": 0.06,
                "vision": False,
            },
            "gpt-4-turbo": {
                "context": 128000,
                "max_out": 4096,
                "in_cost": 0.01,
                "out_cost": 0.03,
                "vision": True,
            },
            "gpt-4-turbo-preview": {
                "context": 128000,
                "max_out": 4096,
                "in_cost": 0.01,
                "out_cost": 0.03,
                "vision": True,
            },
            "gpt-3.5-turbo": {
                "context": 16385,
                "max_out": 4096,
                "in_cost": 0.0005,
                "out_cost": 0.0015,
                "vision": False,
            },
        }
        
        # Get config for this model, default to gpt-4 if unknown
        config = configs.get(self.model, configs["gpt-4"])
        
        return ModelInfo(
            provider="openai",
            model_id=self.model,
            context_window=config["context"],
            max_output_tokens=config["max_out"],
            supports_streaming=True,
            supports_vision=config["vision"],
            supports_functions=True,
            input_cost_per_1k=config["in_cost"],
            output_cost_per_1k=config["out_cost"],
            rate_limit_rpm=500,   # Default tier limit
            rate_limit_tpm=90000,  # Default tier limit
        )
