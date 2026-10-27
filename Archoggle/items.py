from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ArchoggleWorld
    
    
    
ITEM_NAME_TO_ID = {}

DEFAULT_ITEM_NAME_CLASSIFICATION = {}

class ArchoggleItem(Item):
    game = "Archoggle"
    

def get_random_filler_name(world: ArchoggleWorld) -> str:
    print("Temp")
    
def create_item_with_correct_classification(world: ArchoggleWorld, name: str) -> ArchoggleItem:
    classifiction = DEFAUITEM_NAME_CLASSIFICATION[name]
    return ArchoggleLT_Item(nme, classifiction, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: ArchoggleWorld) -> None:
    itempool: list[Item] = []