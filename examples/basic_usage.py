"""Basic usage example for GSR Test library.

This example shows how to:
1. Create an OpenAI adapter
2. Get model information
3. Count tokens
4. Generate a response
5. Estimate costs
"""

import asyncio
import os
from gsr_test import OpenAIAdapter


async def main():
    #Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print(" Please set OPENAI_API_KEY environment variable")
        print("   export OPENAI_API_KEY='your-key-here'")
        return
    
    print("GSR Test - Basic Usage Example\n")
    
    #Create adapter
    print("Creating OpenAI adapter...")
    adapter = OpenAIAdapter(api_key=api_key, model="gpt-4")
    
    #Get model information
    print("\n Model Information:")
    info = adapter.get_model_info()
    print(f"   Provider: {info.provider}")
    print(f"   Model: {info.model_id}")
    print(f"   Context Window: {info.context_window:,} tokens")
    print(f"   Max Output: {info.max_output_tokens:,} tokens")
    print(f"   Supports Streaming: {info.supports_streaming}")
    print(f"   Supports Vision: {info.supports_vision}")
    print(f"   Input Cost: ${info.input_cost_per_1k}/1k tokens")
    print(f"   Output Cost: ${info.output_cost_per_1k}/1k tokens")
    
    #Test token counting
    prompt = "What is the capital of France?"
    tokens = adapter.count_tokens(prompt)
    print(f"\n🔢 Token Count:")
    print(f"   Prompt: '{prompt}'")
    print(f"   Tokens: {tokens}")
    
    #Estimate cost
    estimated_cost = adapter.estimate_cost(prompt, expected_output=20)
    print(f"\n Cost Estimation:")
    print(f"   Estimated cost: ${estimated_cost:.6f}")
    
    #Generate response
    print(f"\n💬 Generating response...")
    response = await adapter.generate(prompt)
    
    print(f"\n Response received:")
    print(f"   Content: {response.content}")
    print(f"   Prompt tokens: {response.prompt_tokens}")
    print(f"   Completion tokens: {response.completion_tokens}")
    print(f"   Total tokens: {response.total_tokens}")
    print(f"   Latency: {response.latency_ms:.2f}ms")
    print(f"   Finish reason: {response.finish_reason}")
    
    #Calculate actual cost
    actual_cost = (
        (response.prompt_tokens / 1000) * info.input_cost_per_1k +
        (response.completion_tokens / 1000) * info.output_cost_per_1k
    )
    print(f"   Actual cost: ${actual_cost:.6f}")
    
    #Test streaming
    print(f"\n🌊 Streaming response to: 'Count to 5'")
    print("   ", end="", flush=True)
    
    async for chunk in adapter.generate_stream("Count to 5"):
        print(chunk, end="", flush=True)
    
    print("\n\n Example complete!")


if __name__ == "__main__":
    asyncio.run(main())
