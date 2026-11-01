from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ArchoggleWorld
    
    
LOCATION_NAME_TO_ID = {
    "Score 1 Points": 1,
    "Score 2 Points": 2,
    "Score 3 Points": 3,
    "Score 4 Points": 4,
    "Score 5 Points": 5,
    "score 6 Points": 6,
    "Score 7 Points": 7,
    "Score 8 Points": 8,
    "Score 9 Points": 9,
    "Score 10 Points": 10,
    "Score 11 Points": 11,
    "Score 12 Points": 12,
    "Score 13 Points": 13,
    "Score 14 Points": 14,
    "Score 15 Points": 15,
    "Score 16 Points": 16,
    "Score 17 Points": 17,
    "Score 18 Points": 18,
    "Score 19 Points": 19,
    "Score 20 Points": 20,
    "Score 21 Points": 21,
    "Score 22 Points": 22,
    "Score 23 Points": 23,
    "Score 24 Points": 24,
    "Score 25 Points": 25,
    "Score 26 Points": 26,
    "Score 27 Points": 27,
    "Score 28 Points": 28,
    "Score 29 Points": 29,
    "Score 30 Points": 30,
    "Score 31 Points": 31,
    "Score 32 Points": 32,
    "Score 33 Points": 33,
    "Score 34 Points": 34,
    "Score 35 Points": 35,
    "Score 36 Points": 36,
    "Score 37 Points": 37,
    "Score 38 Points": 38,
    "Score 39 Points": 39,          
    "Score 40 Points": 40, 
    "Score 41 Points": 41,
    "Score 42 Points": 42,
    "Score 43 Points": 43,
    "Score 44 Points": 44,
    "Score 45 Points": 45,
    "Score 46 Points": 46,
    "Score 47 Points": 47,
    "Score 48 Points": 48,
    "Score 49 Points": 49,
    "Score 50 Points": 50,
    "Score 51 Points": 51,
    "Score 52 Points": 52,
    "Score 53 Points": 53,
    "Score 54 Points": 54,
    "Score 55 Points": 55,
    "Score 56 Points": 56,
    "Score 57 Points": 57,
    "Score 58 Points": 58,
    "Score 59 Poings": 59,
    "Score 61 Points": 61,
    "Score 62 Points": 62,
    "Score 63 Points": 63,
    "Score 64 Points": 64,
    "Score 65 Poins" 65,
    "Score 66 Points": 66,
    "Score 67 Poins" 67,
    "Score 68 Points": 68,
    "Score 69 Points": 69,
    "Score 70 Points": 70,
    "Score 71 Points": 71,
    "Score 72 Points": 72,
    "Score 73 Points": 73,
    "Score 74 Points": 74,
    "Score 75 Points": 75,
    "Score 76 Points": 76,
    "Score 77 Points": 77,
    "Score 78 Points": 78,
    "Score 79 Points": 79,
    "Score 80 Points": 80,
    "Score 81 Points": 81,
    "Score 82 Points": 82,
    "Score 83 Points": 83,
    "Score 84 Points": 84,
    "Score 85 Points": 85,
    "Soore 86 Points": 86,
    "Score 87 Points": 87,
    "Score 88 Points": 88,
    "Score 89 Points": 89,
    "Score 90 Poings" 90,
    "Score 91 Points": 91,




         
 }

class ArchoggleLocation(Location):
    game = "Archoggle"
    

def create_all_locations(world: ArchoggleWorld) -> None:
    create_locations(world)
    
    
def create_locations(world: ArchoggleWorld) -> None:
    for x in range(1, (world.options.needed_points.value + 1)):