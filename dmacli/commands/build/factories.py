"""Factory classes for creating builders."""

from pathlib import Path
from typing import Type

from dmacli.commands.build.builders import Builder, ModificationBuilder, PackBuilder
from dmacli.commands.build.strategies import (
    FPackerBuilderStrategy,
    AddonBuilderStrategy,
    PboPackerBuilderStrategy,
    BohemiaBinarizeStrategy,
)


class BaseBuilderFactory:
    """Base factory class for creating builders."""
    
    def __init__(self, builder_class: Type[Builder]):
        self._builder_class = builder_class
        self._strategies = {
            'fpacker': (FPackerBuilderStrategy(), BohemiaBinarizeStrategy()),
            'addonbuilder': (AddonBuilderStrategy(), BohemiaBinarizeStrategy()),
            'pbopacker': (PboPackerBuilderStrategy(), BohemiaBinarizeStrategy()),
        }
        
    def get_builder(self, builder_type: str, source: Path, destination: Path, cache: bool) -> Builder:
        """Get a builder instance.
        
        Args:
            builder_type: Type of builder to create
            source: Source directory
            destination: Destination directory
            cache: Whether to use caching
            
        Returns:
            Builder instance
            
        Raises:
            ValueError: If builder type is invalid
        """
        strategies = self._strategies.get(builder_type)
        if not strategies:
            raise ValueError(f'Invalid builder type: {builder_type}')
            
        builder_strategy, binarize_strategy = strategies
        return self._builder_class(
            builder_strategy=builder_strategy,
            binarize_strategy=binarize_strategy,
            source=source,
            destination=destination,
            cache=cache
        )


class ModificationBuilderFactory(BaseBuilderFactory):
    """Factory for creating modification builders."""
    
    def __init__(self):
        super().__init__(ModificationBuilder)


class PackBuilderFactory(BaseBuilderFactory):
    """Factory for creating pack builders."""
    
    def __init__(self):
        super().__init__(PackBuilder)
