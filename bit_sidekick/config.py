"""Configuration management for the Bit-Block Sidekick."""

from typing import Dict, Any, Optional
import yaml
import os


class SidekickConfig:
    """Configuration manager for the Sidekick agent."""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the configuration manager.

        Args:
            config_path: Path to the configuration file. If None, uses default config.
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults."""
        if self.config_path and os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                return yaml.safe_load(f) or {}
        return self._default_config()

    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            "agent": {
                "name": "Bit-Block Sidekick",
                "version": "0.1.0",
                "domain_awareness": True,
                "auto_configure": True,
                "self_audit": True,
            },
            "analysis": {
                "enabled": True,
                "security_checks": True,
                "optimization_checks": True,
                "compliance_checks": True,
            },
            "automation": {
                "auto_fix": False,
                "require_approval": True,
                "dry_run": True,
            },
            "cloud": {
                "providers": ["aws", "azure", "gcp"],
                "regions": [],
            },
        }

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.

        Args:
            key: Configuration key (supports dot notation, e.g., 'agent.name')
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        keys = key.split(".")
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        return value

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.

        Args:
            key: Configuration key (supports dot notation)
            value: Value to set
        """
        keys = key.split(".")
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value

    def save(self, path: Optional[str] = None) -> None:
        """
        Save configuration to file.

        Args:
            path: Path to save configuration. If None, uses config_path.
        """
        save_path = path or self.config_path
        if save_path:
            with open(save_path, "w") as f:
                yaml.dump(self.config, f, default_flow_style=False)
