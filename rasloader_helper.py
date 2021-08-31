from enum import Enum
import pandas as pd

START_RAS_LINE = "*RAS_DATA_START\n" # Begins every file.
END_RAS_LINE = "*RAS_DATA_END\n"
END_FILE_LINE = "*DSC_DATA_END\n" # Meaning of this tag is rather obscure.
START_HEADER_LINE = "*RAS_HEADER_START\n"
END_HEADER_LINE = "*RAS_HEADER_END\n"
START_INT_LINE = "*RAS_INT_START\n" # Begins intensity sections
END_INT_LINE = "*RAS_INT_END\n"
AXIS_DATA_INDICATOR = "*MEAS_COND_AXIS_"

class ScanTypes(Enum):
    SCAN1D = 1
    SCAN2D = 2

class CodeNotCompleteException(Exception):
    pass

class UnexpectedLineException(Exception):
    pass

class HeaderIntPair:
    def __init__(self,header_lines,int_lines):
        self.__metadata_raw = dict()
        axis_columns = ['name_internal',
                        'name',
                        'offset',
                        'position',
                        'resolution',
                        'state',
                        'unit']
        axis_dtypes =  [str,
                        str,
                        float,
                        object,
                        float,
                        str,
                        str]
        self.__axisdata_raw = pd.DataFrame(columns = axis_columns,dtype=axis_dtypes)
        self.__intdata_raw = pd.DataFrame(columns=['x','y'],dtype=float)
        for line in header_lines:
            if AXIS_DATA_INDICATOR in line:
                self.__parse_line_axis()
            else:
                self.__parse_line_metadata()
        for line in int_lines:
            self.__parse_line_int(line)

    def __parse_line_metadata(self, line):
        key = self.__get_header_key(line)
        value = self.__get_header_value(line)
        self.__metadata_raw[key] = value

    def __parse_line_axis(self, line):
        number = self.__get_axis_number(line)
        column = self.__get_axis_column(line)
        value = self.__get_axis_value(line)
        self.__axisdata_raw.loc[number,column] = value
        raise CodeNotCompleteException
    
    def __parse_line_int(self, line):
        raise CodeNotCompleteException

    def __get_header_key(self, line):
        raise CodeNotCompleteException

    def __get_header_value(self, line):
        raise CodeNotCompleteException

    def __get_axis_number(self,line):
        raise CodeNotCompleteException

    def __get_axis_column(self,line):
        raise CodeNotCompleteException

    def __get_axis_value(self,line):
        raise CodeNotCompleteException

    def __get_int_x(self, line):
        raise CodeNotCompleteException

    def __get_int_y(self, line):
        raise CodeNotCompleteException

    def get_metadata_final(self):
        raise CodeNotCompleteException

    def get_axisdata_final(self):
        raise CodeNotCompleteException
    
    def get_intdata_final(self):
        raise CodeNotCompleteException
