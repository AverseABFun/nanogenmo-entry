from enum import Enum, auto

class Room(Enum):
    EMPTY = auto()
    START = auto()
    
    CORRIDOR22 = auto()
    CORRIDOR32 = auto()
    CORRIDOR42 = auto()
    CORRIDOR23 = auto()
    CORRIDOR43 = auto()
    CORRIDOR24 = auto()
    CORRIDOR44 = auto()
    CORRIDOR25 = auto()
    CORRIDOR45 = auto()
    
    LUNCHROOM13 = auto()
    LAB54 = auto()
    ENGINES14 = auto()
    ENGINES54 = auto()
    PLANT26 = auto()
    WATERGEN46 = auto()