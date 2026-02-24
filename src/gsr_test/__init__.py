"""GSR Test - Governance, Safety, and Reliability Testing for AI Models.

A comprehensive framework for testing AI models for safety vulnerabilities,
security issues, reliability problems, and governance compliance.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Core imports
from gsr_test.core.adapter import ModelAdapter
from gsr_test.core.response import Response, ModelInfo, TestResult
from gsr_test.core.config import TestConfig

# Adapter imports
from gsr_test.adapters.openai import OpenAIAdapter

__all__ = [
    # Core classes
    "ModelAdapter",
    "Response",
    "ModelInfo",
    "TestResult",
    "TestConfig",
    # Adapters
    "OpenAIAdapter",
]
