"""Core AI agent for the Bit-Block Sidekick."""

from typing import Dict, Any, Optional
import logging
from bit_sidekick.config import SidekickConfig
from bit_sidekick.modules.analyzer import InfrastructureAnalyzer
from bit_sidekick.modules.configurator import AutoConfigurator
from bit_sidekick.modules.auditor import SelfAuditor


logger = logging.getLogger(__name__)


class SidekickAgent:
    """
    The main AI agent that orchestrates infrastructure management.

    This agent is domain-aware and capable of analyzing, optimizing,
    and maintaining cloud environments with minimal human input.
    """

    def __init__(self, config: Optional[SidekickConfig] = None):
        """
        Initialize the Sidekick agent.

        Args:
            config: Configuration object. If None, uses default configuration.
        """
        self.config = config or SidekickConfig()
        self.analyzer = InfrastructureAnalyzer(self.config)
        self.configurator = AutoConfigurator(self.config)
        self.auditor = SelfAuditor(self.config)
        logger.info("Bit-Block Sidekick initialized")

    def analyze_infrastructure(self, starter_pack_path: str) -> Dict[str, Any]:
        """
        Analyze a Bit-Block Starter Pack and assess the infrastructure.

        Args:
            starter_pack_path: Path to the starter pack configuration

        Returns:
            Analysis report with findings and recommendations
        """
        logger.info(f"Analyzing infrastructure at {starter_pack_path}")
        return self.analyzer.analyze(starter_pack_path)

    def auto_configure(
        self, starter_pack_path: str, target_environment: str = "dev"
    ) -> Dict[str, Any]:
        """
        Auto-configure infrastructure based on the starter pack.

        Args:
            starter_pack_path: Path to the starter pack configuration
            target_environment: Target environment (dev, staging, prod)

        Returns:
            Configuration result with applied changes
        """
        logger.info(f"Auto-configuring infrastructure for {target_environment}")
        return self.configurator.configure(starter_pack_path, target_environment)

    def self_audit(self, infrastructure_path: str) -> Dict[str, Any]:
        """
        Perform self-audit of the infrastructure for security and optimization.

        Args:
            infrastructure_path: Path to the infrastructure configuration

        Returns:
            Audit report with security findings and optimization recommendations
        """
        logger.info(f"Running self-audit on {infrastructure_path}")
        return self.auditor.audit(infrastructure_path)

    def optimize(self, infrastructure_path: str) -> Dict[str, Any]:
        """
        Optimize the infrastructure based on analysis and audit findings.

        Args:
            infrastructure_path: Path to the infrastructure configuration

        Returns:
            Optimization report with applied changes
        """
        logger.info(f"Optimizing infrastructure at {infrastructure_path}")

        # First, analyze the current state
        analysis = self.analyzer.analyze(infrastructure_path)

        # Run security and optimization audit
        audit = self.auditor.audit(infrastructure_path)

        # Apply optimizations if auto_fix is enabled
        optimizations = []
        if self.config.get("automation.auto_fix"):
            optimizations = self.configurator.apply_optimizations(
                infrastructure_path, audit.get("recommendations", [])
            )

        return {
            "status": "completed",
            "analysis": analysis,
            "audit": audit,
            "optimizations_applied": optimizations,
        }

    def transform_starter_pack(
        self, starter_pack_path: str, target_environment: str = "dev"
    ) -> Dict[str, Any]:
        """
        Transform a Bit-Block Starter Pack into a living, thinking system.

        This is the main method that orchestrates the complete transformation:
        1. Analyzes the starter pack
        2. Auto-configures for the target environment
        3. Performs self-audit
        4. Applies optimizations

        Args:
            starter_pack_path: Path to the starter pack
            target_environment: Target environment

        Returns:
            Complete transformation report
        """
        logger.info(f"Transforming starter pack: {starter_pack_path}")

        result = {
            "status": "in_progress",
            "starter_pack": starter_pack_path,
            "target_environment": target_environment,
        }

        try:
            # Step 1: Analyze
            logger.info("Step 1: Analyzing starter pack")
            result["analysis"] = self.analyze_infrastructure(starter_pack_path)

            # Step 2: Auto-configure
            logger.info("Step 2: Auto-configuring infrastructure")
            result["configuration"] = self.auto_configure(starter_pack_path, target_environment)

            # Step 3: Self-audit
            logger.info("Step 3: Running self-audit")
            result["audit"] = self.self_audit(starter_pack_path)

            # Step 4: Optimize if enabled
            if self.config.get("analysis.optimization_checks"):
                logger.info("Step 4: Applying optimizations")
                result["optimization"] = self.optimize(starter_pack_path)

            result["status"] = "completed"
            logger.info("Transformation completed successfully")

        except Exception as e:
            logger.error(f"Transformation failed: {e}")
            result["status"] = "failed"
            result["error"] = str(e)

        return result
