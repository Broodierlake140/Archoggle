from dataclasses import dataclass
from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class NeededPoints(Range):
    """
    Points Neded To Goal
    """
    
    display_name = "Points Needed"
    range_start = 5
    range_end = 100
    default = 50

@dataclass
class ArchoggleOptions(PerGameCommonOptions):
    needed_points: NeededPoints
    


    
