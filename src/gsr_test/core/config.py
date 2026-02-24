"""Configuration management for GSR Test."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import yaml
from pathlib import Path


@dataclass
class TestConfig:
    """Configuration for test execution.
    
    This class controls which tests to run, execution parameters,
    thresholds, and reporting options.
    """
    
    # Test categories to run
    run_safety: bool = True
    run_security: bool = True
    run_reliability: bool = True
    run_bias: bool = True
    run_hallucination: bool = True
    run_quality: bool = True
    
    # Execution settings
    parallel: bool = True
    max_workers: int = 5
    timeout_seconds: int = 30
    
    # Thresholds (0-100 scale)
    safety_threshold: float = 80.0
    quality_threshold: float = 70.0
    reliability_threshold: float = 75.0
    
    # Reporting
    report_format: List[str] = field(default_factory=lambda: ["html", "json"])
    output_dir: str = "./gsr_reports"
    
    @classmethod
    def from_yaml(cls, path: str) -> "TestConfig":
        """Load configuration from a YAML file.
        
        Args:
            path: Path to YAML configuration file
            
        Returns:
            TestConfig instance with loaded settings
        """
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return cls(**data)
    
    def to_yaml(self, path: str) -> None:
        """Save configuration to a YAML file.
        
        Args:
            path: Path where YAML file should be saved
        """
        with open(path, 'w') as f:
            yaml.dump(self.__dict__, f, default_flow_style=False)
    
    @classmethod
    def default(cls) -> "TestConfig":
        """Create a configuration with default settings.
        
        Returns:
            TestConfig with all defaults
        """
        return cls()
