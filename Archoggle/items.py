from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ArchoggleWorld
    
    
    
ITEM_NAME_TO_ID = {
    "Progressive Block": 1000,
    "Block 1": 1001,
    "Block 2": 1002,
    "Block 3": 1003,
    "Block 4": 1004,
    "Block 5": 1005,
    "Block 6": 1006,
    "Block 7": 1007,
    "Block 8": 1008,
    "Block 9": 1009,
    "Block 10": 1010,
    "Block 11": 1011,
    "Block 12": 1012,
    "Block 13": 1013,
    "Block 14": 1014,
    "Block 15": 1015,
    "Block 16": 1016,
    "Show First Letter": 2000,
}

DEFAULT_ITEM_NAME_CLASSIFICATION = {
    "Progressive Block": ItemClassification.progression,
    "Block 1": ItemClassification.progression,
    "Block 2": ItemClassification.progression,
    "Block 3": ItemClassification.progression,
    "Block 4": ItemClassification.progression,
    "Block 5": ItemClassification.progression,
    "Block 6": ItemClassification.progression,
    "Block 7": ItemClassification.progression,
    "Block 8": ItemClassification.progression,
    "Block 9": ItemClassification.progression,
    "Block 10": ItemClassification.progression,
    "Block 11": ItemClassification.progression,
    "Block 12": ItemClassification.progression,
    "Block 13": ItemClassification.progression,
    "Block 14": ItemClassification.progression,
    "Block 15": ItemClassification.progression,
    "Block 16": ItemClassification.progression,
    "Show First Letter": ItemClassification.filler
}

class ArchoggleItem(Item):
    game = "Archoggle"
    

def get_random_filler_name(world: ArchoggleWorld) -> str:
    return("Show First Letter")
    
def create_item_with_correct_classification(world: ArchoggleWorld, name: str) -> ArchoggleItem:
    classifiction = DEFAULT_ITEM_NAME_CLASSIFICATION[name]
    return ArchoggleItem(name, classifiction, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: ArchoggleWorld) -> None:
    itempool: list[Item] = []