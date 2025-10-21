"""Command-line interface for the Bit-Block Sidekick."""

import click
import logging
import sys
from bit_sidekick import SidekickAgent, SidekickConfig
from bit_sidekick import __version__


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version=__version__)
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True),
    help="Path to configuration file",
)
@click.pass_context
def main(ctx: click.Context, config: str) -> None:
    """
    Bit-Block Sidekick: A lightweight, domain-aware AI agent for infrastructure automation.

    Transform your Bit-Block Starter Packs into living, thinking systems.
    """
    ctx.ensure_object(dict)
    ctx.obj["config"] = SidekickConfig(config) if config else SidekickConfig()
    ctx.obj["agent"] = SidekickAgent(ctx.obj["config"])


@main.command()
@click.argument("starter_pack_path", type=click.Path(exists=True))
@click.pass_context
def analyze(ctx: click.Context, starter_pack_path: str) -> None:
    """Analyze a Bit-Block Starter Pack or infrastructure configuration."""
    agent = ctx.obj["agent"]
    click.echo(f"Analyzing: {starter_pack_path}")

    try:
        result = agent.analyze_infrastructure(starter_pack_path)
        _display_analysis_result(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@main.command()
@click.argument("starter_pack_path", type=click.Path(exists=True))
@click.option(
    "--environment",
    "-e",
    type=click.Choice(["dev", "staging", "prod"]),
    default="dev",
    help="Target environment",
)
@click.pass_context
def configure(ctx: click.Context, starter_pack_path: str, environment: str) -> None:
    """Auto-configure infrastructure for a target environment."""
    agent = ctx.obj["agent"]
    click.echo(f"Configuring for {environment} environment: {starter_pack_path}")

    try:
        result = agent.auto_configure(starter_pack_path, environment)
        _display_configuration_result(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@main.command()
@click.argument("infrastructure_path", type=click.Path(exists=True))
@click.pass_context
def audit(ctx: click.Context, infrastructure_path: str) -> None:
    """Perform self-audit of infrastructure for security and optimization."""
    agent = ctx.obj["agent"]
    click.echo(f"Auditing: {infrastructure_path}")

    try:
        result = agent.self_audit(infrastructure_path)
        _display_audit_result(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@main.command()
@click.argument("infrastructure_path", type=click.Path(exists=True))
@click.pass_context
def optimize(ctx: click.Context, infrastructure_path: str) -> None:
    """Optimize infrastructure based on analysis and audit findings."""
    agent = ctx.obj["agent"]
    click.echo(f"Optimizing: {infrastructure_path}")

    try:
        result = agent.optimize(infrastructure_path)
        _display_optimization_result(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@main.command()
@click.argument("starter_pack_path", type=click.Path(exists=True))
@click.option(
    "--environment",
    "-e",
    type=click.Choice(["dev", "staging", "prod"]),
    default="dev",
    help="Target environment",
)
@click.pass_context
def transform(ctx: click.Context, starter_pack_path: str, environment: str) -> None:
    """
    Transform a Bit-Block Starter Pack into a living, thinking system.

    This command orchestrates the complete transformation process:
    analysis, configuration, audit, and optimization.
    """
    agent = ctx.obj["agent"]
    click.echo("=" * 60)
    click.echo("Bit-Block Sidekick: Transformation Process")
    click.echo("=" * 60)
    click.echo(f"Starter Pack: {starter_pack_path}")
    click.echo(f"Environment: {environment}")
    click.echo("=" * 60)

    try:
        result = agent.transform_starter_pack(starter_pack_path, environment)
        _display_transformation_result(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def _display_analysis_result(result: dict) -> None:
    """Display analysis results in a user-friendly format."""
    click.echo("\n" + "=" * 60)
    click.echo("ANALYSIS RESULTS")
    click.echo("=" * 60)

    click.echo(f"\nPath: {result.get('path')}")
    click.echo(f"Type: {result.get('type', 'unknown')}")

    if result.get("resources"):
        click.echo(f"\nResources found: {len(result['resources'])}")
        for resource in result["resources"][:5]:  # Show first 5
            click.echo(f"  - {resource.get('name')} ({resource.get('type')})")

    if result.get("findings"):
        click.echo(f"\nFindings: {len(result['findings'])}")
        for finding in result["findings"]:
            click.echo(f"  [{finding.get('type')}] {finding.get('message')}")

    if result.get("recommendations"):
        click.echo(f"\nRecommendations: {len(result['recommendations'])}")
        for rec in result["recommendations"]:
            click.echo(f"  - {rec.get('message')}")


def _display_configuration_result(result: dict) -> None:
    """Display configuration results."""
    click.echo("\n" + "=" * 60)
    click.echo("CONFIGURATION RESULTS")
    click.echo("=" * 60)

    click.echo(f"\nStatus: {result.get('status')}")
    click.echo(f"Environment: {result.get('environment')}")

    if result.get("configurations"):
        click.echo(f"\nConfigurations applied: {len(result['configurations'])}")
        for config in result["configurations"]:
            click.echo(f"  - {config.get('type')}")


def _display_audit_result(result: dict) -> None:
    """Display audit results."""
    click.echo("\n" + "=" * 60)
    click.echo("AUDIT RESULTS")
    click.echo("=" * 60)

    click.echo(f"\nStatus: {result.get('status')}")
    click.echo(f"Risk Score: {result.get('risk_score')}/100")

    if result.get("security_findings"):
        click.echo(f"\nSecurity Findings: {len(result['security_findings'])}")
        for finding in result["security_findings"]:
            severity = finding.get("severity", "unknown").upper()
            click.echo(f"  [{severity}] {finding.get('message')}")

    if result.get("optimization_findings"):
        click.echo(f"\nOptimization Findings: {len(result['optimization_findings'])}")
        for finding in result["optimization_findings"]:
            click.echo(f"  - {finding.get('message')}")

    if result.get("recommendations"):
        click.echo(f"\nRecommendations: {len(result['recommendations'])}")
        for rec in result["recommendations"][:5]:  # Show first 5
            priority = rec.get("priority", "medium").upper()
            click.echo(f"  [{priority}] {rec.get('action')}")


def _display_optimization_result(result: dict) -> None:
    """Display optimization results."""
    click.echo("\n" + "=" * 60)
    click.echo("OPTIMIZATION RESULTS")
    click.echo("=" * 60)

    click.echo(f"\nStatus: {result.get('status')}")

    if result.get("optimizations_applied"):
        click.echo(f"\nOptimizations applied: {len(result['optimizations_applied'])}")
        for opt in result["optimizations_applied"]:
            click.echo(f"  - {opt.get('status')}")


def _display_transformation_result(result: dict) -> None:
    """Display transformation results."""
    click.echo("\n" + "=" * 60)
    click.echo("TRANSFORMATION COMPLETE")
    click.echo("=" * 60)

    click.echo(f"\nStatus: {result.get('status')}")

    if result.get("status") == "completed":
        click.echo("\n✓ Analysis completed")
        click.echo("✓ Configuration applied")
        click.echo("✓ Security audit completed")

        if result.get("optimization"):
            click.echo("✓ Optimizations applied")

        click.echo("\nYour Bit-Block Starter Pack has been transformed into a")
        click.echo("living, thinking system ready for deployment!")
    elif result.get("status") == "failed":
        click.echo(f"\n✗ Transformation failed: {result.get('error')}")


if __name__ == "__main__":
    main()
