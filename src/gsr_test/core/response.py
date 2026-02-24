"""Core response models for GSR Test framework."""

from dataclasses import dataclass
from typing import Any, Dict, Optional
from datetime import datetime

@dataclass
class Response:
    """Standardized response from any AI model."""
    
    # What every response needs:
    content: str                    # The text
    model: str                      # Which model generated that text
    
    # Token usage for cost calculations
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    
    # Metadata
    finish_reason: str              # "stop", "length", etc.
    latency_ms: float              # How long it took
    timestamp: datetime             # When it was generated
    
    # Extras
    metadata: Dict[str, Any]       # Provider-specific info
    raw_response: Any              # For debugging


@dataclass
class ModelInfo:
    """Information about a model's capabilities."""
    
    # Identify model
    provider: str                   # "openai", "anthropic", etc.
    model_id: str                   # "gpt-4", "claude-3-opus"
    
    # Capabilities
    context_window: int            # Max tokens (e.g., 128000)
    max_output_tokens: int         # Max response length
    supports_streaming: bool
    supports_vision: bool
    supports_functions: bool
    
    # Costs
    input_cost_per_1k: float       # Per 1000 input tokens
    output_cost_per_1k: float      # Per 1000 output tokens
    
    # Limits
    rate_limit_rpm: Optional[int] = None  # Requests per minute
    rate_limit_tpm: Optional[int] = None  # Tokens per minute


@dataclass
class TestResult:
    """Result from a single test."""
    
    test_name: str
    category: str                   # "safety", "quality", "bias", etc.
    passed: bool
    score: float                    # 0-100
    severity: str                   # "critical", "high", "medium", "low"
    message: str
    details: Dict[str, Any]
    timestamp: datetime
