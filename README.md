# GSR Test

**Governance, Safety, and Reliability Testing for AI Models**

A comprehensive Python framework for testing AI models for safety vulnerabilities, security issues, reliability problems, and governance compliance before deployment.

## Features

- **Model-Agnostic**: Works with OpenAI, Anthropic, AWS Bedrock, Azure, and more
- **Comprehensive Testing**: Safety, security, reliability, bias, hallucination detection
- **Easy to Use**: Simple API for running tests on any AI model
- **Extensible**: Plugin architecture for adding custom tests and adapters
- **Production-Ready**: Designed for CI/CD integration and compliance reporting

## Quick Start

### Installation

```bash
pip install -e .
```

Or with specific provider support:

```bash
pip install -e ".[openai]"      # OpenAI support
pip install -e ".[anthropic]"   # Anthropic support
pip install -e ".[all]"         # All providers
```

### Basic Usage

```python
import asyncio
from gsr_test import OpenAIAdapter

async def main():
    # Create an adapter for your AI model
    adapter = OpenAIAdapter(api_key="your-api-key", model="gpt-4")
    
    # Get model information
    info = adapter.get_model_info()
    print(f"Model: {info.model_id}")
    print(f"Context window: {info.context_window} tokens")
    
    # Generate a response
    response = await adapter.generate("What is 2+2?")
    print(f"Response: {response.content}")
    print(f"Tokens used: {response.total_tokens}")
    print(f"Latency: {response.latency_ms}ms")

if __name__ == "__main__":
    asyncio.run(main())
```

## Project Structure

```
gsr-test/
├── src/gsr_test/
│   ├── core/           # Core functionality (adapters, config, etc.)
│   ├── adapters/       # Provider-specific adapters
│   ├── integrations/   # External tool integrations
│   ├── metrics/        # Evaluation metrics
│   ├── reports/        # Report generation
│   └── cli/            # Command-line interface
├── tests/              # Test suite
├── examples/           # Usage examples
└── docs/               # Documentation
```

## Current Status

✅ Core adapter architecture  
✅ OpenAI adapter implementation  
✅ Configuration system  
✅ Response models  

🚧 GSRTester orchestration (in progress)  
🚧 Test scenarios (in progress)  
🚧 Additional adapters (in progress)  

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/ tests/
isort src/ tests/
```

## License

Property of Aanlytica

## Contributing

Contributions welcome! (Analytica Only)
