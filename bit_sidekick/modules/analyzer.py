"""Infrastructure analysis module for the Bit-Block Sidekick."""

from typing import Dict, List, Any
import os
import yaml
import logging
from bit_sidekick.config import SidekickConfig


logger = logging.getLogger(__name__)


class InfrastructureAnalyzer:
    """Analyzes Bit-Block Starter Packs and infrastructure configurations."""

    def __init__(self, config: SidekickConfig):
        """
        Initialize the analyzer.

        Args:
            config: Sidekick configuration
        """
        self.config = config

    def analyze(self, starter_pack_path: str) -> Dict[str, Any]:
        """
        Analyze a starter pack or infrastructure configuration.

        Args:
            starter_pack_path: Path to the configuration

        Returns:
            Analysis report with findings
        """
        logger.info(f"Starting analysis of {starter_pack_path}")

        result = {
            "path": starter_pack_path,
            "exists": os.path.exists(starter_pack_path),
            "resources": [],
            "findings": [],
            "recommendations": [],
        }

        if not result["exists"]:
            result["findings"].append({
                "type": "error",
                "message": f"Path does not exist: {starter_pack_path}",
            })
            return result

        # Determine if it's a file or directory
        if os.path.isfile(starter_pack_path):
            result["type"] = "file"
            result.update(self._analyze_file(starter_pack_path))
        elif os.path.isdir(starter_pack_path):
            result["type"] = "directory"
            result.update(self._analyze_directory(starter_pack_path))

        # Add domain-specific recommendations
        result["recommendations"].extend(self._generate_recommendations(result))

        logger.info(f"Analysis complete. Found {len(result['findings'])} findings")
        return result

    def _analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze a single configuration file."""
        result: Dict[str, Any] = {"resources": [], "findings": []}

        try:
            with open(file_path, "r") as f:
                if file_path.endswith((".yml", ".yaml")):
                    content = yaml.safe_load(f)
                    result["format"] = "yaml"
                    result["content"] = content
                    result["resources"] = self._extract_resources(content)
                elif file_path.endswith(".json"):
                    import json
                    content = json.load(f)
                    result["format"] = "json"
                    result["content"] = content
                    result["resources"] = self._extract_resources(content)
                else:
                    result["format"] = "unknown"
                    result["findings"].append({
                        "type": "warning",
                        "message": "Unknown file format",
                    })
        except Exception as e:
            result["findings"].append({
                "type": "error",
                "message": f"Failed to parse file: {e}",
            })

        return result

    def _analyze_directory(self, dir_path: str) -> Dict[str, Any]:
        """Analyze a directory containing multiple configuration files."""
        result: Dict[str, Any] = {"resources": [], "findings": [], "files": []}

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith((".yml", ".yaml", ".json")):
                    file_path = os.path.join(root, file)
                    file_analysis = self._analyze_file(file_path)
                    result["files"].append({
                        "path": file_path,
                        "analysis": file_analysis,
                    })
                    result["resources"].extend(file_analysis.get("resources", []))
                    result["findings"].extend(file_analysis.get("findings", []))

        return result

    def _extract_resources(self, content: Any) -> List[Dict[str, Any]]:
        """Extract infrastructure resources from configuration."""
        resources = []

        if isinstance(content, dict):
            # Check for common infrastructure patterns
            if "resources" in content:
                resources.extend(self._parse_resources(content["resources"]))
            if "services" in content:
                resources.extend(self._parse_services(content["services"]))
            if "infrastructure" in content:
                resources.extend(self._parse_infrastructure(content["infrastructure"]))

        return resources

    def _parse_resources(self, resources_config: Any) -> List[Dict[str, Any]]:
        """Parse resources from configuration."""
        resources = []
        if isinstance(resources_config, dict):
            for name, config in resources_config.items():
                resource_type = "unknown"
                if isinstance(config, dict):
                    resource_type = config.get("type", "unknown")
                resources.append({
                    "name": name,
                    "type": resource_type,
                    "config": config,
                })
        elif isinstance(resources_config, list):
            for item in resources_config:
                if isinstance(item, dict):
                    resources.append({
                        "name": item.get("name", "unnamed"),
                        "type": item.get("type", "unknown"),
                        "config": item,
                    })
        return resources

    def _parse_services(self, services_config: Any) -> List[Dict[str, Any]]:
        """Parse services from configuration."""
        services = []
        if isinstance(services_config, dict):
            for name, config in services_config.items():
                services.append({
                    "name": name,
                    "type": "service",
                    "config": config,
                })
        return services

    def _parse_infrastructure(self, infra_config: Any) -> List[Dict[str, Any]]:
        """Parse infrastructure components from configuration."""
        components = []
        if isinstance(infra_config, dict):
            for name, config in infra_config.items():
                components.append({
                    "name": name,
                    "type": "infrastructure",
                    "config": config,
                })
        return components

    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate domain-aware recommendations based on analysis."""
        recommendations = []

        # Check for security best practices
        if self.config.get("analysis.security_checks"):
            recommendations.extend(self._security_recommendations(analysis))

        # Check for optimization opportunities
        if self.config.get("analysis.optimization_checks"):
            recommendations.extend(self._optimization_recommendations(analysis))

        return recommendations

    def _security_recommendations(self, analysis: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate security-related recommendations."""
        recommendations = []

        resources = analysis.get("resources", [])

        # Check for missing encryption
        for resource in resources:
            config = resource.get("config", {})
            if isinstance(config, dict) and not config.get("encryption"):
                recommendations.append({
                    "type": "security",
                    "resource": resource.get("name"),
                    "message": "Consider enabling encryption for this resource",
                })

        return recommendations

    def _optimization_recommendations(self, analysis: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate optimization recommendations."""
        recommendations = []

        resources = analysis.get("resources", [])

        # Suggest resource optimization
        if len(resources) > 10:
            recommendations.append({
                "type": "optimization",
                "message": "Consider consolidating resources to reduce complexity",
            })

        return recommendations
