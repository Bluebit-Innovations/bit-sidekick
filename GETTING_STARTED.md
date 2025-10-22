# Getting Started with Bit-Block Sidekick

## What is Bit-Block Sidekick?

Bit-Block Sidekick is an intelligent AI agent that transforms your infrastructure configuration templates (Starter Packs) into production-ready, self-auditing, and auto-configuring systems. Think of it as your DevOps co-pilot that helps you build secure, optimized cloud infrastructure with minimal effort.

## Quick Start (5 Minutes)

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/Bluebit-Innovations/bit-sidekick.git
cd bit-sidekick

# Install the package
pip install -e .
```

### 2. Verify Installation

```bash
bit-sidekick --version
```

You should see: `bit-sidekick, version 0.1.0`

### 3. Try Your First Analysis

```bash
bit-sidekick analyze examples/starter-packs/web-app/infrastructure.yml
```

This will analyze a sample web application infrastructure and provide insights.

### 4. Transform a Starter Pack

```bash
bit-sidekick transform examples/starter-packs/web-app/infrastructure.yml --environment prod
```

This runs the complete transformation process: analysis, configuration, audit, and optimization.

## Understanding the Output

### Analysis Output

The analysis shows:
- **Resources Found**: Infrastructure components detected
- **Findings**: Issues or concerns identified
- **Recommendations**: Suggested improvements

### Audit Output

The audit provides:
- **Risk Score**: Overall security/compliance score (0-100)
- **Security Findings**: Security vulnerabilities and concerns
- **Optimization Findings**: Performance and cost optimization opportunities
- **Recommendations**: Prioritized action items

### Configuration Output

The configuration shows:
- **Environment**: Target environment (dev/staging/prod)
- **Configurations Applied**: Settings applied for the environment

## Common Use Cases

### Use Case 1: New Project Setup

You're starting a new microservices project:

```bash
# 1. Analyze the microservices starter pack
bit-sidekick analyze examples/starter-packs/microservices/infrastructure.yml

# 2. Configure for development
bit-sidekick configure examples/starter-packs/microservices/infrastructure.yml --environment dev

# 3. When ready for production
bit-sidekick transform examples/starter-packs/microservices/infrastructure.yml --environment prod
```

### Use Case 2: Security Audit

You want to audit your existing infrastructure:

```bash
# Run a comprehensive security audit
bit-sidekick audit path/to/your/infrastructure.yml
```

Review the findings and address high-priority security issues first.

### Use Case 3: Environment Migration

Moving from staging to production:

```bash
# 1. Configure for production
bit-sidekick configure path/to/config.yml --environment prod

# 2. Review the changes
# (Output shows production-optimized settings)

# 3. Apply optimizations
bit-sidekick optimize path/to/config.yml
```

### Use Case 4: Cost Optimization

Reduce infrastructure costs:

```bash
# 1. Run analysis to identify optimization opportunities
bit-sidekick analyze path/to/config.yml

# 2. Review optimization recommendations
# (Look for cost-related suggestions)

# 3. Apply optimizations
bit-sidekick optimize path/to/config.yml
```

## Creating Your Own Starter Pack

### Basic Structure

Create a file `my-app.yml`:

```yaml
name: my-application
version: 1.0.0
description: My application infrastructure

infrastructure:
  compute:
    type: container
    image: my-app:latest
    replicas: 2
    resources:
      cpu: 1
      memory: 2Gi

  database:
    type: postgresql
    version: "14"
    storage: 20Gi

services:
  api:
    name: api-service
    port: 8080
    health_check: /health

monitoring:
  enabled: true
  
security:
  encryption_at_rest: true
```

### Analyze Your Config

```bash
bit-sidekick analyze my-app.yml
```

The Sidekick will provide recommendations based on your configuration.

## Using the Python API

You can also use the Sidekick programmatically:

```python
from bit_sidekick import SidekickAgent

# Create an agent
agent = SidekickAgent()

# Analyze your infrastructure
analysis = agent.analyze_infrastructure("my-app.yml")
print(f"Found {len(analysis['resources'])} resources")

# Auto-configure for production
config = agent.auto_configure("my-app.yml", "prod")
print(f"Status: {config['status']}")

# Run security audit
audit = agent.self_audit("my-app.yml")
print(f"Risk Score: {audit['risk_score']}/100")

# Complete transformation
result = agent.transform_starter_pack("my-app.yml", "prod")
if result['status'] == 'completed':
    print("Transformation successful!")
```

## Configuration Options

### Custom Configuration File

Create `sidekick-config.yml`:

```yaml
agent:
  name: "My Custom Sidekick"
  domain_awareness: true
  auto_configure: true

analysis:
  security_checks: true
  optimization_checks: true
  compliance_checks: true

automation:
  auto_fix: false        # Set to true to auto-apply fixes
  dry_run: true          # Simulate changes without applying
  require_approval: true # Require approval for changes

cloud:
  providers:
    - aws
    - azure
    - gcp
```

Use it with:

```bash
bit-sidekick --config sidekick-config.yml transform my-app.yml --environment prod
```

## Development Workflow

### Recommended Workflow

1. **Start Small**: Begin with the `dev` environment
   ```bash
   bit-sidekick configure my-app.yml --environment dev
   ```

2. **Iterate**: Make changes based on analysis feedback
   ```bash
   bit-sidekick analyze my-app.yml
   ```

3. **Test**: Move to staging when ready
   ```bash
   bit-sidekick configure my-app.yml --environment staging
   ```

4. **Audit**: Run security audit before production
   ```bash
   bit-sidekick audit my-app.yml
   ```

5. **Deploy**: Transform for production
   ```bash
   bit-sidekick transform my-app.yml --environment prod
   ```

## Tips and Best Practices

### 1. Always Start with Analysis
Before making any changes, understand your current state:
```bash
bit-sidekick analyze <path>
```

### 2. Review Audit Findings
Pay special attention to high-severity security findings:
```bash
bit-sidekick audit <path> | grep HIGH
```

### 3. Use Environment Progression
Follow the dev → staging → prod progression to catch issues early.

### 4. Enable Dry-Run Mode
Test changes without applying them:
```yaml
automation:
  dry_run: true
```

### 5. Track Your Configurations
Keep your starter packs in version control (Git) to track changes over time.

### 6. Regular Audits
Schedule periodic security audits, especially after major changes.

## Troubleshooting

### Problem: "Path does not exist"
**Solution**: Check that the file path is correct and the file exists.

### Problem: "Failed to parse file"
**Solution**: Validate your YAML/JSON syntax. Use a linter like `yamllint`.

### Problem: No recommendations shown
**Solution**: Your infrastructure might already be optimized! Try analyzing a different configuration.

### Problem: Import errors
**Solution**: Ensure the package is installed:
```bash
pip install -e .
```

## Next Steps

1. **Explore Examples**: Check out `examples/starter-packs/` for more complex configurations
2. **Read Architecture**: See `ARCHITECTURE.md` for technical details
3. **Run Tests**: Try `pytest tests/` to understand the test suite
4. **Contribute**: Fork the repo and submit improvements!

## Getting Help

- **Documentation**: See `README.md` and `ARCHITECTURE.md`
- **Examples**: Check `examples/starter-packs/` for templates
- **Issues**: Report bugs on GitHub
- **Questions**: Open a discussion on GitHub

## What's Next?

Now that you know the basics, try:
- Creating your own starter pack
- Integrating with your CI/CD pipeline
- Customizing the configuration for your needs
- Contributing back to the project

Happy building! 🚀
