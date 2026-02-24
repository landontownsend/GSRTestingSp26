"""Abstract base class for model adapters."""

from abc import ABC, abstractmethod
from typing import AsyncIterator, Optional
from gsr_test.core.response import Response, ModelInfo


class ModelAdapter(ABC):
    """Base class for all model adapters.
    
    All concrete adapter implementations must implement these methods.
    This ensures a consistent interface across all AI providers.
    """
    
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> Response:
        """Generate a response from the model.
        
        Args:
            prompt: The input text/prompt to send to the model
            **kwargs: Provider-specific parameters (temperature, max_tokens, etc.)
            
        Returns:
            Response object with standardized format
        """
        pass
    
    @abstractmethod
    async def generate_stream(self, prompt: str, **kwargs) -> AsyncIterator[str]:
        """Generate a streaming response (tokens arrive one at a time).
        
        Args:
            prompt: The input text/prompt to send to the model
            **kwargs: Provider-specific parameters
            
        Yields:
            Text chunks as they arrive from the model
        """
        pass
    
    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """Count how many tokens a text contains.
        
        Each provider uses different tokenizers, so this must be
        implemented per-adapter.
        
        Args:
            text: Text to count tokens for
            
        Returns:
            Number of tokens
        """
        pass
    
    @abstractmethod
    def get_model_info(self) -> ModelInfo:
        """Get information about the model's capabilities.
        
        Returns:
            ModelInfo with details about context window, costs, limits, etc.
        """
        pass
    
    # Helper methods (implemented here, not abstract)
    
    def estimate_cost(self, prompt: str, expected_output: int = 100) -> float:
        """Estimate the cost of a request before running it.
        
        Args:
            prompt: The prompt to send
            expected_output: Expected number of output tokens (default: 100)
            
        Returns:
            Estimated cost in USD
        """
        info = self.get_model_info()
        input_tokens = self.count_tokens(prompt)
        
        input_cost = (input_tokens / 1000) * info.input_cost_per_1k
        output_cost = (expected_output / 1000) * info.output_cost_per_1k
        
        return input_cost + output_cost
