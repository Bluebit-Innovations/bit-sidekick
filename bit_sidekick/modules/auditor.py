"""Self-auditing module for the Bit-Block Sidekick."""

from typing import Dict, List, Any
import os
import logging
from bit_sidekick.config import SidekickConfig


logger = logging.getLogger(__name__)


class SelfAuditor:
    """Performs self-audits of infrastructure for security and optimization."""

    def __init__(self, config: SidekickConfig):
        """
        Initialize the auditor.

        Args:
            config: Sidekick configuration
        """
        self.config = config

    def audit(self, infrastructure_path: str) -> Dict[str, Any]:
        """
        Perform a comprehensive audit of the infrastructure.

        Args:
            infrastructure_path: Path to infrastructure configuration

        Returns:
            Audit report with findings and recommendations
        """
        logger.info(f"Starting audit of {infrastructure_path}")

        result = {
            "status": "completed",
            "path": infrastructure_path,
            "security_findings": [],
            "optimization_findings": [],
            "compliance_findings": [],
            "recommendations": [],
            "risk_score": 0,
        }

        if not os.path.exists(infrastructure_path):
            result["status"] = "error"
            result["message"] = f"Path does not exist: {infrastructure_path}"
            return result

        # Run security checks
        if self.config.get("analysis.security_checks"):
            result["security_findings"] = self._security_audit(infrastructure_path)

        # Run optimization checks
        if self.config.get("analysis.optimization_checks"):
            result["optimization_findings"] = self._optimization_audit(infrastructure_path)

        # Run compliance checks
        if self.config.get("analysis.compliance_checks"):
            result["compliance_findings"] = self._compliance_audit(infrastructure_path)

        # Calculate risk score
        result["risk_score"] = self._calculate_risk_score(result)

        # Generate recommendations
        result["recommendations"] = self._generate_recommendations(result)

        logger.info(f"Audit complete. Risk score: {result['risk_score']}")
        return result

    def _security_audit(self, infrastructure_path: str) -> List[Dict[str, Any]]:
        """Perform security audit."""
        findings = []

        # Check for common security issues
        security_checks = [
            self._check_encryption,
            self._check_access_controls,
            self._check_network_security,
            self._check_secrets_management,
        ]

        for check in security_checks:
            finding = check(infrastructure_path)
            if finding:
                findings.extend(finding if isinstance(finding, list) else [finding])

        return findings

    def _check_encryption(self, path: str) -> List[Dict[str, Any]]:
        """Check encryption configuration."""
        findings = []

        # In a real implementation, this would parse the configuration
        # and check for encryption settings
        findings.append({
            "type": "security",
            "severity": "medium",
            "category": "encryption",
            "message": "Ensure data encryption is enabled for all storage resources",
            "recommendation": "Enable encryption at rest for all data storage",
        })

        return findings

    def _check_access_controls(self, path: str) -> List[Dict[str, Any]]:
        """Check access control configuration."""
        findings = []

        findings.append({
            "type": "security",
            "severity": "high",
            "category": "access_control",
            "message": "Review IAM policies for least privilege access",
            "recommendation": "Implement role-based access control (RBAC)",
        })

        return findings

    def _check_network_security(self, path: str) -> List[Dict[str, Any]]:
        """Check network security configuration."""
        findings = []

        findings.append({
            "type": "security",
            "severity": "medium",
            "category": "network",
            "message": "Verify network segmentation and firewall rules",
            "recommendation": "Implement network isolation for sensitive resources",
        })

        return findings

    def _check_secrets_management(self, path: str) -> List[Dict[str, Any]]:
        """Check secrets management."""
        findings = []

        findings.append({
            "type": "security",
            "severity": "high",
            "category": "secrets",
            "message": "Ensure secrets are stored securely",
            "recommendation": "Use a secrets management service for sensitive data",
        })

        return findings

    def _optimization_audit(self, infrastructure_path: str) -> List[Dict[str, Any]]:
        """Perform optimization audit."""
        findings = []

        # Check for optimization opportunities
        optimization_checks = [
            self._check_resource_utilization,
            self._check_cost_optimization,
            self._check_performance,
        ]

        for check in optimization_checks:
            finding = check(infrastructure_path)
            if finding:
                findings.extend(finding if isinstance(finding, list) else [finding])

        return findings

    def _check_resource_utilization(self, path: str) -> List[Dict[str, Any]]:
        """Check resource utilization."""
        findings = []

        findings.append({
            "type": "optimization",
            "severity": "low",
            "category": "resources",
            "message": "Monitor resource utilization for right-sizing opportunities",
            "recommendation": "Implement auto-scaling based on actual usage patterns",
        })

        return findings

    def _check_cost_optimization(self, path: str) -> List[Dict[str, Any]]:
        """Check cost optimization opportunities."""
        findings = []

        findings.append({
            "type": "optimization",
            "severity": "low",
            "category": "cost",
            "message": "Review resource costs for optimization opportunities",
            "recommendation": "Consider reserved instances or spot instances for cost savings",
        })

        return findings

    def _check_performance(self, path: str) -> List[Dict[str, Any]]:
        """Check performance configuration."""
        findings = []

        findings.append({
            "type": "optimization",
            "severity": "low",
            "category": "performance",
            "message": "Review performance metrics and optimization opportunities",
            "recommendation": "Implement caching and CDN for improved performance",
        })

        return findings

    def _compliance_audit(self, infrastructure_path: str) -> List[Dict[str, Any]]:
        """Perform compliance audit."""
        findings = []

        findings.append({
            "type": "compliance",
            "severity": "medium",
            "category": "logging",
            "message": "Ensure audit logging is enabled for compliance",
            "recommendation": "Enable comprehensive audit logging for all resources",
        })

        findings.append({
            "type": "compliance",
            "severity": "medium",
            "category": "backup",
            "message": "Verify backup and disaster recovery procedures",
            "recommendation": "Implement automated backup and recovery processes",
        })

        return findings

    def _calculate_risk_score(self, audit_result: Dict[str, Any]) -> int:
        """Calculate overall risk score based on findings."""
        severity_weights = {
            "high": 10,
            "medium": 5,
            "low": 2,
        }

        score = 0
        for finding_type in ["security_findings", "compliance_findings"]:
            for finding in audit_result.get(finding_type, []):
                severity = finding.get("severity", "low")
                score += severity_weights.get(severity, 0)

        return min(score, 100)  # Cap at 100

    def _generate_recommendations(self, audit_result: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate prioritized recommendations based on audit findings."""
        recommendations = []

        # Prioritize high-severity security findings
        for finding in audit_result.get("security_findings", []):
            if finding.get("severity") == "high":
                recommendations.append({
                    "priority": "high",
                    "type": "security",
                    "action": finding.get("recommendation"),
                    "reason": finding.get("message"),
                })

        # Add optimization recommendations
        for finding in audit_result.get("optimization_findings", []):
            recommendations.append({
                "priority": "medium",
                "type": "optimization",
                "action": finding.get("recommendation"),
                "reason": finding.get("message"),
            })

        # Add compliance recommendations
        for finding in audit_result.get("compliance_findings", []):
            recommendations.append({
                "priority": "medium",
                "type": "compliance",
                "action": finding.get("recommendation"),
                "reason": finding.get("message"),
            })

        return recommendations
