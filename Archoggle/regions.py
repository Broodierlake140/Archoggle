from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from rule_builder.rules import Rule

from dataclasses import dataclass

if TYPE_CHECKING:
    from .world import ArchoggleWorld
    
    
def create_and_connect_regions(world: ArchoggleWorld) -> None:
    
    @dataclass()
    class Regions_Ents():
        entrance: str
        rule: Rule

    Region: dict[str, list[Regions_Ents]] = {
        "": [
            
        ],
        
        
    }