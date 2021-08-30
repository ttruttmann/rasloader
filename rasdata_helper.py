from enum import Enum

START_RAS_LINE = "*RAS_DATA_START\n" # Begins every file.
END_RAS_LINE = "*RAS_DATA_END\n"
END_FILE_LINE = "*DSC_DATA_END\n" # Meaning is rather obscure.
START_HEADER_LINE = "*RAS_HEADER_START\n"
END_HEADER_LINE = "*RAS_HEADER_END\n"
START_INT_LINE = "*RAS_INT_START\n" # Begins intensity sections
END_INT_LINE = "*RAS_INT_END\n"

class ScanTypes(Enum):
    SCAN1D = 1
    SCAN2D = 2

class CodeNotCompleteException(Exception):
    pass

class UnexpectedLineException(Exception):
    pass

class HeaderIntPair:
    def __init__(self,header_lines,int_lines):
        raise CodeNotCompleteException
