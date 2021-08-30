from enum import Enum

class ScanTypes(Enum):
    SCAN1D = 1
    SCAN2D = 2

class CodeNotCompleteException(Exception):
    pass

class UnexpectedLineException(Exception):
    pass

START_RAS_LINE = "*RAS_DATA_START\n"
END_RAS_LINE = "*RAS_DATA_END\n"
END_FILE_LINE = "*DSC_DATA_END\n"
START_HEADER_LINE = "*RAS_HEADER_START\n"
END_HEADER_LINE = "*RAS_HEADER_END\n"
START_INT_LINE = "*RAS_INT_START\n"
END_INT_LINE = "*RAS_INT_END\n"