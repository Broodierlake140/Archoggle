from collections.abc import Mapping
from typing import Any

from worlds.Autoworld import World
from . import options as archoggle_options

class ArchoggleWorld(World):
    game = "Archoggle"
    
    options_dataclass = archoggle_options.ArchoggleOptions
    options: archoggle_options.ArchoggleOptions
    
    



