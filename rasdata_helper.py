from enum import Enum

class ScanTypes(Enum):
    SCAN1D = 1
    SCAN2D = 2

class CodeNotCompleteException(Exception):
    pass

class UnexpectedLineException(Exception):
    pass

LINES_TO_SKIP = [
    "*RAS_DATA_START",
    "*RAS_HEADER_START",
    "*RAS_HEADER_END",
    "*RAS_INT_START",
    "*RAS_INT_END"
]

LINES_TO_END = [
    "*RAS_DATA_END",
    "*DSC_DATA_END"
]