# Bit-Block Sidekick

The Bit-Block Sidekick is a lightweight, domain-aware AI agent built to help startups, engineers, and DevOps teams hit the ground running with secure, self-auditing, and auto-configuring infrastructure.

Unlike static templates or boilerplate repositories, the Sidekick transforms your Bit-Block Starter Packs into living, thinking systems — capable of analyzing, optimizing, and maintaining your cloud environments with minimal human input.

## Features

🤖 **Domain-Aware AI Agent**: Intelligent understanding of infrastructure patterns and best practices

🔒 **Self-Auditing**: Automatic security and compliance checks with actionable recommendations

⚙️ **Auto-Configuration**: Smart configuration for different environments (dev, staging, prod)

📊 **Infrastructure Analysis**: Deep analysis of starter packs with optimization suggestions

🚀 **Living, Thinking Systems**: Transforms static configurations into adaptive infrastructure

🛡️ **Security First**: Built-in security checks, encryption recommendations, and access control validation

## Installation

```bash
pip install -e .
```

Or with development dependencies:

```bash
pip install -e ".[dev]"
```

## Quick Start

### 1. Analyze a Starter Pack

```bash
bit-sidekick analyze examples/starter-packs/web-app/infrastructure.yml
```

### 2. Auto-Configure for an Environment

```bash
bit-sidekick configure examples/starter-packs/web-app/infrastructure.yml --environment prod
```

### 3. Audit Your Infrastructure

```bash
bit-sidekick audit examples/starter-packs/web-app/infrastructure.yml
```

### 4. Complete Transformation

Transform your starter pack into a living, thinking system:

```bash
bit-sidekick transform examples/starter-packs/web-app/infrastructure.yml --environment prod
```

## Usage

### Command-Line Interface

The Sidekick provides a comprehensive CLI for all operations:

```bash
# Show help
bit-sidekick --help

# Analyze infrastructure
bit-sidekick analyze <path>

# Configure for environment
bit-sidekick configure <path> --environment [dev|staging|prod]

# Run security audit
bit-sidekick audit <path>

# Optimize infrastructure
bit-sidekick optimize <path>

# Complete transformation
bit-sidekick transform <path> --environment [dev|staging|prod]
```

### Python API

You can also use the Sidekick programmatically:

```python
from bit_sidekick import SidekickAgent, SidekickConfig

# Initialize the agent
agent = SidekickAgent()

# Analyze a starter pack
analysis = agent.analyze_infrastructure("path/to/starter-pack.yml")

# Auto-configure for production
config = agent.auto_configure("path/to/starter-pack.yml", "prod")

# Run security audit
audit = agent.self_audit("path/to/starter-pack.yml")

# Complete transformation
result = agent.transform_starter_pack("path/to/starter-pack.yml", "prod")
```

## Configuration

Create a `sidekick-config.yml` file to customize behavior:

```yaml
agent:
  name: "My Sidekick"
  domain_awareness: true
  auto_configure: true
  self_audit: true

analysis:
  enabled: true
  security_checks: true
  optimization_checks: true
  compliance_checks: true

automation:
  auto_fix: false
  require_approval: true
  dry_run: true

cloud:
  providers:
    - aws
    - azure
    - gcp
```

Then use it with:

```bash
bit-sidekick --config sidekick-config.yml transform <path>
```

## Starter Pack Examples

The repository includes example starter packs:

- **web-app**: Basic web application infrastructure
- **microservices**: Microservices architecture with service mesh
- **data-platform**: Data processing and analytics platform

Explore them in `examples/starter-packs/`.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/Bluebit-Innovations/bit-sidekick.git
cd bit-sidekick

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black bit_sidekick/
```

### Type Checking

```bash
mypy bit_sidekick/
```

## Architecture

The Sidekick is built on three core modules:

1. **Analyzer**: Analyzes infrastructure configurations and generates insights
2. **Configurator**: Auto-configures infrastructure for different environments
3. **Auditor**: Performs security and optimization audits

These modules work together through the main `SidekickAgent` to provide a complete infrastructure management solution.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Support

For issues, questions, or contributions, please visit:
https://github.com/Bluebit-Innovations/bit-sidekick
