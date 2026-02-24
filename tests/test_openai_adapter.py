"""Tests for OpenAI adapter."""

import pytest
from gsr_test.adapters.openai import OpenAIAdapter


def test_token_counting():
    """Test that token counting works."""
    adapter = OpenAIAdapter(api_key="fake-key-for-testing", model="gpt-4")
    
    # Test basic token counting
    tokens = adapter.count_tokens("Hello world")
    assert tokens > 0
    assert isinstance(tokens, int)
    
    # Longer text should have more tokens
    tokens_long = adapter.count_tokens("Hello world! This is a longer sentence.")
    assert tokens_long > tokens


def test_model_info():
    """Test model info retrieval."""
    adapter = OpenAIAdapter(api_key="fake-key-for-testing", model="gpt-4")
    
    info = adapter.get_model_info()
    
    # Check basic info
    assert info.provider == "openai"
    assert info.model_id == "gpt-4"
    assert info.context_window == 8192
    assert info.max_output_tokens == 4096
    
    # Check capabilities
    assert info.supports_streaming is True
    assert info.supports_functions is True
    
    # Check costs are set
    assert info.input_cost_per_1k > 0
    assert info.output_cost_per_1k > 0


def test_cost_estimation():
    """Test cost estimation."""
    adapter = OpenAIAdapter(api_key="fake-key-for-testing", model="gpt-4")
    
    prompt = "What is 2+2?"
    cost = adapter.estimate_cost(prompt, expected_output=50)
    
    # Cost should be positive
    assert cost > 0
    
    # Longer prompt should cost more
    long_prompt = prompt * 100
    cost_long = adapter.estimate_cost(long_prompt, expected_output=50)
    assert cost_long > cost


def test_different_models():
    """Test that different models have different configs."""
    gpt4 = OpenAIAdapter(api_key="fake-key", model="gpt-4")
    gpt4_turbo = OpenAIAdapter(api_key="fake-key", model="gpt-4-turbo")
    gpt35 = OpenAIAdapter(api_key="fake-key", model="gpt-3.5-turbo")
    
    info_gpt4 = gpt4.get_model_info()
    info_gpt4_turbo = gpt4_turbo.get_model_info()
    info_gpt35 = gpt35.get_model_info()
    
    # GPT-4 Turbo has larger context window
    assert info_gpt4_turbo.context_window > info_gpt4.context_window
    
    # GPT-3.5 is cheaper
    assert info_gpt35.input_cost_per_1k < info_gpt4.input_cost_per_1k


# Note: We're not testing generate() or generate_stream() here
# because they require a real API key and make actual API calls.
# Those should be tested manually or in integration tests with real credentials.
