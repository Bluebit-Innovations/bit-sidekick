"""Tests for the analyzer module."""

import pytest
import tempfile
import os
import yaml
from bit_sidekick.config import SidekickConfig
from bit_sidekick.modules.analyzer import InfrastructureAnalyzer


@pytest.fixture
def analyzer():
    """Create a test analyzer."""
    config = SidekickConfig()
    return InfrastructureAnalyzer(config)


@pytest.fixture
def temp_yaml_file():
    """Create a temporary YAML configuration file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "test.yml")
        config_data = {
            "resources": {
                "web_server": {"type": "compute", "replicas": 2},
                "database": {"type": "postgresql", "encryption": True},
            },
        }
        with open(config_path, "w") as f:
            yaml.dump(config_data, f)
        yield config_path


def test_analyzer_initialization():
    """Test analyzer initialization."""
    config = SidekickConfig()
    analyzer = InfrastructureAnalyzer(config)
    assert analyzer is not None
    assert analyzer.config is not None


def test_analyze_nonexistent_path(analyzer):
    """Test analyzing non-existent path."""
    result = analyzer.analyze("/nonexistent/path")
    assert result["exists"] is False
    assert len(result["findings"]) > 0


def test_analyze_yaml_file(analyzer, temp_yaml_file):
    """Test analyzing YAML file."""
    result = analyzer.analyze(temp_yaml_file)
    assert result["exists"] is True
    assert result["type"] == "file"
    assert result["format"] == "yaml"
    assert len(result["resources"]) > 0


def test_extract_resources(analyzer):
    """Test resource extraction."""
    content = {
        "resources": {
            "server": {"type": "compute"},
            "db": {"type": "database"},
        }
    }
    resources = analyzer._extract_resources(content)
    assert len(resources) == 2
    assert resources[0]["name"] in ["server", "db"]


def test_security_recommendations(analyzer):
    """Test security recommendations."""
    analysis = {
        "resources": [
            {"name": "db", "config": {"encryption": False}},
        ]
    }
    recommendations = analyzer._security_recommendations(analysis)
    assert len(recommendations) > 0
    assert any(r["type"] == "security" for r in recommendations)
