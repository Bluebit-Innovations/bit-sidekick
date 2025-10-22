"""
Bit-Block Sidekick: A lightweight, domain-aware AI agent for infrastructure automation.

The Sidekick transforms Bit-Block Starter Packs into living, thinking systems capable of
analyzing, optimizing, and maintaining cloud environments with minimal human input.
"""

__version__ = "0.1.0"
__author__ = "Bluebit Innovations"

from bit_sidekick.agent import SidekickAgent
from bit_sidekick.config import SidekickConfig

__all__ = ["SidekickAgent", "SidekickConfig"]
