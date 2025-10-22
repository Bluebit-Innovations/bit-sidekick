"""Tests for the SidekickAgent."""

import pytest
import tempfile
import os
import yaml
from bit_sidekick.agent import SidekickAgent
from bit_sidekick.config import SidekickConfig


@pytest.fixture
def agent():
    """Create a test agent."""
    return SidekickAgent()


@pytest.fixture
def temp_config_file():
    """Create a temporary configuration file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "test_config.yml")
        config_data = {
            "infrastructure": {
                "compute": {"type": "container", "replicas": 2},
                "database": {"type": "postgresql"},
            },
            "services": {
                "web": {"name": "web-service", "port": 80},
            },
        }
        with open(config_path, "w") as f:
            yaml.dump(config_data, f)
        yield config_path


def test_agent_initialization():
    """Test agent initialization."""
    agent = SidekickAgent()
    assert agent is not None
    assert agent.config is not None
    assert agent.analyzer is not None
    assert agent.configurator is not None
    assert agent.auditor is not None


def test_analyze_infrastructure_nonexistent(agent):
    """Test analyzing non-existent path."""
    result = agent.analyze_infrastructure("/nonexistent/path")
    assert result["exists"] is False


def test_analyze_infrastructure_valid(agent, temp_config_file):
    """Test analyzing valid configuration."""
    result = agent.analyze_infrastructure(temp_config_file)
    assert result["exists"] is True
    assert result["type"] == "file"


def test_auto_configure(agent, temp_config_file):
    """Test auto-configuration."""
    result = agent.auto_configure(temp_config_file, "dev")
    assert result["status"] == "success"
    assert result["environment"] == "dev"
    assert len(result["configurations"]) > 0


def test_self_audit(agent, temp_config_file):
    """Test self-audit."""
    result = agent.self_audit(temp_config_file)
    assert result["status"] == "completed"
    assert "security_findings" in result
    assert "optimization_findings" in result
    assert "risk_score" in result


def test_optimize(agent, temp_config_file):
    """Test optimization."""
    result = agent.optimize(temp_config_file)
    assert result["status"] == "completed"
    assert "analysis" in result
    assert "audit" in result


def test_transform_starter_pack(agent, temp_config_file):
    """Test complete transformation."""
    result = agent.transform_starter_pack(temp_config_file, "dev")
    assert result["status"] == "completed"
    assert result["starter_pack"] == temp_config_file
    assert result["target_environment"] == "dev"
    assert "analysis" in result
    assert "configuration" in result
    assert "audit" in result
