from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ArchoggleWorld
    
    
LOCATION_NAME_TO_ID = {}