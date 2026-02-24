# GSR Test - Quick Start Guide

## What You Have Now

You have a complete foundational structure for the GSR Test library:

### ✅ Completed Files:

1. **Core Module** (`src/gsr_test/core/`)
   - `response.py` - Response, ModelInfo, TestResult data models
   - `adapter.py` - ModelAdapter abstract base class
   - `config.py` - TestConfig for configuration management

2. **Adapters** (`src/gsr_test/adapters/`)
   - `openai.py` - Complete OpenAI adapter implementation

3. **Package Files**
   - `src/gsr_test/__init__.py` - Main package initialization
   - All `__init__.py` files for submodules

4. **Project Files**
   - `setup.py` - Installation configuration
   - `requirements.txt` - Dependencies
   - `README.md` - Project documentation
   - `.gitignore` - Git ignore rules

5. **Examples**
   - `examples/basic_usage.py` - Complete usage example
   - `examples/gsr_config.yaml` - Configuration example

6. **Tests**
   - `tests/test_openai_adapter.py` - Unit tests for OpenAI adapter

---

## How to Use This Project

### Step 1: Set Up Your Environment

```bash
# Navigate to the project directory
cd gsr-test/

# Create a virtual environment (recommended)
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install the package in development mode
pip install -e ".[openai,dev]"
```

### Step 2: Test It Works

```bash
# Run the unit tests
pytest tests/

# Should see tests passing ✓
```

### Step 3: Try the Example

```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-key-here"

# Run the example
python examples/basic_usage.py

# You should see:
# - Model information
# - Token counting
# - Cost estimation
# - Generated response
# - Streaming example
```

### Step 4: Use It in Your Code

```python
from gsr_test import OpenAIAdapter
import asyncio

async def main():
    adapter = OpenAIAdapter(api_key="your-key", model="gpt-4")
    response = await adapter.generate("Hello!")
    print(response.content)

asyncio.run(main())
```

---

## What to Build Next

### Week 1 (This Week):
- [ ] Verify everything installs correctly
- [ ] Run the example with your API key
- [ ] Get comfortable with the adapter pattern
- [ ] Make any small tweaks needed

### Week 2 (Next Week):
- [ ] Create `GSRTester` class in `src/gsr_test/core/tester.py`
- [ ] Add safety test scenarios in `src/gsr_test/tests/safety_scenarios.py`
- [ ] Create basic evaluators in `src/gsr_test/metrics/safety.py`
- [ ] Build test orchestration

### Week 3:
- [ ] Add Anthropic adapter (your teammate?)
- [ ] Add more test scenarios
- [ ] Integrate external tools (PyRIT, etc.)

### Week 4:
- [ ] Report generation
- [ ] CLI tool
- [ ] Documentation

---

## Project Structure Explained

```
gsr-test/
│
├── src/gsr_test/          # The actual library code
│   ├── core/              # Core functionality
│   │   ├── adapter.py     # ModelAdapter base class
│   │   ├── response.py    # Data models
│   │   └── config.py      # Configuration
│   │
│   ├── adapters/          # Provider adapters
│   │   └── openai.py      # OpenAI implementation
│   │
│   ├── integrations/      # External tools (TODO)
│   ├── metrics/           # Evaluators (TODO)
│   ├── reports/           # Report generation (TODO)
│   └── cli/               # Command-line tool (TODO)
│
├── tests/                 # Test suite
│   └── test_openai_adapter.py
│
├── examples/              # Usage examples
│   ├── basic_usage.py
│   └── gsr_config.yaml
│
├── setup.py               # Installation config
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

---

## Common Commands

```bash
# Install package
pip install -e .

# Install with optional dependencies
pip install -e ".[openai,dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=gsr_test

# Format code
black src/ tests/
isort src/ tests/

# Type checking
mypy src/
```

---

## Troubleshooting

### "Module not found: gsr_test"
- Make sure you ran `pip install -e .`
- Check you're in the right directory (should have setup.py)
- Check your virtual environment is activated

### "No module named 'openai'"
- Install OpenAI: `pip install openai tiktoken`
- Or install with extras: `pip install -e ".[openai]"`

### Tests fail
- Check you have pytest installed: `pip install pytest pytest-asyncio`
- Make sure you're running from the project root

---

## Tips for Development

1. **Always work in a virtual environment** - Keeps dependencies isolated
2. **Install in editable mode** (`-e`) - Changes reflect immediately
3. **Write tests as you go** - Easier than writing them later
4. **Use the example file** - Quick way to test changes
5. **Keep it simple** - Build incrementally, test frequently

---

## Next Steps

1. ✅ Get everything installed and working
2. ✅ Run the example successfully
3. 🎯 Start building GSRTester next week
4. 🎯 Add more adapters (Anthropic, etc.)
5. 🎯 Build out the test scenarios

You have a solid foundation! Now you can build the actual testing logic on top of this architecture.
