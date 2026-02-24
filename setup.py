"""Setup configuration for GSR Test library."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() if (this_directory / "README.md").exists() else ""

setup(
    # Basic metadata
    name="gsr-test",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    
    # Description
    description="Governance, Safety, and Reliability Testing for AI Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # URLs
    url="https://github.com/yourusername/gsr-test",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/gsr-test/issues",
        "Documentation": "https://gsr-test.readthedocs.io",
        "Source Code": "https://github.com/yourusername/gsr-test",
    },
    
    # Package discovery
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # Include non-Python files (templates, configs, etc.)
    include_package_data=True,
    package_data={
        "gsr_test": ["reports/templates/*.html", "reports/templates/*.css"],
    },
    
    # Core dependencies
    install_requires=[
        "pydantic>=2.0.0",
        "pyyaml>=6.0",
        "aiohttp>=3.8.0",
        "rich>=13.0.0",
    ],
    
    # Optional dependencies
    extras_require={
        "openai": [
            "openai>=1.0.0",
            "tiktoken>=0.5.0",
        ],
        "anthropic": [
            "anthropic>=0.18.0",
        ],
        "aws": [
            "boto3>=1.28.0",
        ],
        "azure": [
            "azure-ai-contentsafety>=1.0.0",
        ],
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "mypy>=1.4.0",
            "isort>=5.12.0",
        ],
        "all": [
            "openai>=1.0.0",
            "tiktoken>=0.5.0",
            "anthropic>=0.18.0",
            "boto3>=1.28.0",
            "azure-ai-contentsafety>=1.0.0",
        ],
    },
    
    # Command-line scripts
    entry_points={
        "console_scripts": [
            "gsr-test=gsr_test.cli.main:main",
        ],
    },
    
    # Python version requirement
    python_requires=">=3.9",
    
    # PyPI classifiers (for categorization on PyPI)
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    
    # Keywords for PyPI search
    keywords="ai llm testing safety security governance reliability adversarial red-team",
    
    # License
    license="MIT",
)
