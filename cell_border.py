from enum import IntFlag

class CellBorder(IntFlag): 
    HasLeftWall = 1
    HasRightWall = 2
    HasTopWall = 4
    HasBottomWall = 8
    Default = HasLeftWall + HasRightWall + HasTopWall + HasBottomWall
