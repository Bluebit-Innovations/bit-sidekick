"""Auto-configuration module for the Bit-Block Sidekick."""

from typing import Dict, List, Any
import os
import logging
from bit_sidekick.config import SidekickConfig


logger = logging.getLogger(__name__)


class AutoConfigurator:
    """Auto-configures infrastructure based on starter packs and environment."""

    def __init__(self, config: SidekickConfig):
        """
        Initialize the auto-configurator.

        Args:
            config: Sidekick configuration
        """
        self.config = config

    def configure(self, starter_pack_path: str, target_environment: str) -> Dict[str, Any]:
        """
        Auto-configure infrastructure for the target environment.

        Args:
            starter_pack_path: Path to the starter pack
            target_environment: Target environment (dev, staging, prod)

        Returns:
            Configuration result
        """
        logger.info(f"Configuring for {target_environment} environment")

        result = {
            "status": "success",
            "environment": target_environment,
            "configurations": [],
            "changes": [],
        }

        # Check if path exists
        if not os.path.exists(starter_pack_path):
            result["status"] = "error"
            result["message"] = f"Path does not exist: {starter_pack_path}"
            return result

        # Apply environment-specific configurations
        env_config = self._get_environment_config(target_environment)
        result["configurations"].append(env_config)

        # Apply auto-scaling if configured
        if self.config.get("automation.auto_configure"):
            scaling_config = self._configure_auto_scaling(target_environment)
            result["configurations"].append(scaling_config)

        # Apply security configurations
        security_config = self._configure_security(target_environment)
        result["configurations"].append(security_config)

        # Apply monitoring and logging
        monitoring_config = self._configure_monitoring(target_environment)
        result["configurations"].append(monitoring_config)

        logger.info(f"Configuration complete for {target_environment}")
        return result

    def _get_environment_config(self, environment: str) -> Dict[str, Any]:
        """Get environment-specific configuration."""
        env_configs = {
            "dev": {
                "name": "Development Environment",
                "instance_type": "small",
                "replicas": 1,
                "auto_scaling": False,
                "monitoring": "basic",
            },
            "staging": {
                "name": "Staging Environment",
                "instance_type": "medium",
                "replicas": 2,
                "auto_scaling": True,
                "monitoring": "standard",
            },
            "prod": {
                "name": "Production Environment",
                "instance_type": "large",
                "replicas": 3,
                "auto_scaling": True,
                "monitoring": "comprehensive",
            },
        }

        return {
            "type": "environment",
            "config": env_configs.get(environment, env_configs["dev"]),
        }

    def _configure_auto_scaling(self, environment: str) -> Dict[str, Any]:
        """Configure auto-scaling based on environment."""
        scaling_configs = {
            "dev": {
                "enabled": False,
                "min_instances": 1,
                "max_instances": 1,
            },
            "staging": {
                "enabled": True,
                "min_instances": 1,
                "max_instances": 3,
                "target_cpu_utilization": 70,
            },
            "prod": {
                "enabled": True,
                "min_instances": 2,
                "max_instances": 10,
                "target_cpu_utilization": 60,
            },
        }

        return {
            "type": "auto_scaling",
            "config": scaling_configs.get(environment, scaling_configs["dev"]),
        }

    def _configure_security(self, environment: str) -> Dict[str, Any]:
        """Configure security settings."""
        return {
            "type": "security",
            "config": {
                "encryption_at_rest": True,
                "encryption_in_transit": True,
                "network_isolation": True,
                "access_logging": True,
                "security_groups": self._get_security_groups(environment),
            },
        }

    def _get_security_groups(self, environment: str) -> List[Dict[str, Any]]:
        """Get security group configurations."""
        base_rules = [
            {
                "name": "https",
                "protocol": "tcp",
                "port": 443,
                "source": "0.0.0.0/0",
            },
        ]

        if environment == "dev":
            base_rules.append({
                "name": "http",
                "protocol": "tcp",
                "port": 80,
                "source": "0.0.0.0/0",
            })

        return base_rules

    def _configure_monitoring(self, environment: str) -> Dict[str, Any]:
        """Configure monitoring and logging."""
        monitoring_levels = {
            "dev": {
                "metrics": ["cpu", "memory"],
                "logging_level": "info",
                "retention_days": 7,
            },
            "staging": {
                "metrics": ["cpu", "memory", "disk", "network"],
                "logging_level": "info",
                "retention_days": 30,
                "alerts": ["error_rate", "high_cpu"],
            },
            "prod": {
                "metrics": ["cpu", "memory", "disk", "network", "requests"],
                "logging_level": "warning",
                "retention_days": 90,
                "alerts": ["error_rate", "high_cpu", "high_memory", "low_availability"],
            },
        }

        return {
            "type": "monitoring",
            "config": monitoring_levels.get(environment, monitoring_levels["dev"]),
        }

    def apply_optimizations(
        self, infrastructure_path: str, recommendations: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Apply optimization recommendations.

        Args:
            infrastructure_path: Path to infrastructure configuration
            recommendations: List of optimization recommendations

        Returns:
            List of applied optimizations
        """
        applied = []

        if self.config.get("automation.dry_run"):
            logger.info("Running in dry-run mode, not applying changes")
            return applied

        for recommendation in recommendations:
            if recommendation.get("type") == "optimization":
                # In a real implementation, this would apply the actual changes
                applied.append({
                    "recommendation": recommendation,
                    "status": "applied",
                })
                logger.info(f"Applied optimization: {recommendation.get('message')}")

        return applied
