# Example Bit-Block Starter Pack

This directory contains example starter packs that demonstrate how the Bit-Block Sidekick
can transform static configurations into living, thinking systems.

## Available Starter Packs

- **web-app**: Basic web application infrastructure
- **microservices**: Microservices architecture with multiple services
- **data-platform**: Data processing and analytics platform

## Usage

```bash
# Analyze a starter pack
bit-sidekick analyze examples/starter-packs/web-app/infrastructure.yml

# Configure for development environment
bit-sidekick configure examples/starter-packs/web-app/infrastructure.yml --environment dev

# Audit the configuration
bit-sidekick audit examples/starter-packs/web-app/infrastructure.yml

# Complete transformation
bit-sidekick transform examples/starter-packs/web-app/infrastructure.yml --environment prod
```
