from enum import Enum

class ScanTypes(Enum):
    SCAN1D = 1
    SCAN2D = 2

class CodeNotCompleteError(Exception):
    pass
