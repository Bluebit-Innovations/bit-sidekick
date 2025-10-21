"""Tests for the configuration module."""

import pytest
import tempfile
import os
from bit_sidekick.config import SidekickConfig


def test_default_config():
    """Test default configuration."""
    config = SidekickConfig()
    assert config.get("agent.name") == "Bit-Block Sidekick"
    assert config.get("agent.domain_awareness") is True
    assert config.get("analysis.enabled") is True


def test_config_get_nested():
    """Test getting nested configuration values."""
    config = SidekickConfig()
    assert config.get("agent.version") == "0.1.0"
    assert config.get("automation.dry_run") is True


def test_config_get_default():
    """Test getting configuration with default value."""
    config = SidekickConfig()
    assert config.get("nonexistent.key", "default") == "default"


def test_config_set():
    """Test setting configuration values."""
    config = SidekickConfig()
    config.set("agent.name", "Custom Sidekick")
    assert config.get("agent.name") == "Custom Sidekick"


def test_config_set_nested():
    """Test setting nested configuration values."""
    config = SidekickConfig()
    config.set("custom.nested.value", "test")
    assert config.get("custom.nested.value") == "test"


def test_config_save_load():
    """Test saving and loading configuration."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "config.yml")

        # Create and save config
        config1 = SidekickConfig()
        config1.set("agent.name", "Test Sidekick")
        config1.save(config_path)

        # Load config
        config2 = SidekickConfig(config_path)
        assert config2.get("agent.name") == "Test Sidekick"
