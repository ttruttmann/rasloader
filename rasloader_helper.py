from enum import Enum
import pandas as pd

START_RAS_LINE = "*RAS_DATA_START\n" # Begins every file.
END_RAS_LINE = "*RAS_DATA_END\n"
END_FILE_LINE = "*DSC_DATA_END\n" # Meaning of this tag is rather obscure.
START_HEADER_LINE = "*RAS_HEADER_START\n"
END_HEADER_LINE = "*RAS_HEADER_END\n"
START_INT_LINE = "*RAS_INT_START\n" # Begins intensity sections
END_INT_LINE = "*RAS_INT_END\n"

AXIS_DATA_INDICATOR = "MEAS_COND_AXIS_"
STEP_AXIS_INDICATOR = "MEAS_3DE_STEP_AXIS_INTERNAL"
XAXIS_INDICATOR = "MEAS_SCAN_AXIS_X"

class ScanTypes(Enum):
    SCAN1D = 1
    SCAN2D = 2

class CodeNotCompleteException(Exception):
    pass

class UnexpectedLineException(Exception):
    pass

class InconsistentHeaderException(Exception):
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
        self.__axisdata_raw = pd.DataFrame(columns = axis_columns)
        self.__intdata_x = []
        self.__intdata_y = []
        for line in header_lines:
            if AXIS_DATA_INDICATOR in line:
                self.__parse_line_axis(line)
            else:
                self.__parse_line_metadata(line)
        for line in int_lines:
            self.__parse_line_int(line)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    def __parse_line_metadata(self, line):
        key = self.__get_header_key(line)
        value = self.__get_header_value(line)
        self.__metadata_raw[key] = value

    def __parse_line_axis(self, line):
        number = self.__get_axis_index(line)
        column = self.__get_axis_column(line)
        value = self.__get_header_value(line)
        self.__axisdata_raw.loc[number,column] = value
    
    def __parse_line_int(self, intline):
        self.__intdata_x.append(self.__get_x(intline))
        self.__intdata_y.append(self.__get_y(intline))

    def __get_header_key(self, line):
        return(line.split(' ')[0].replace('*',''))

    def __get_header_value(self, line):
        line_without_key = ' '.join(line.split(' ')[1:])
        value_as_string = line_without_key.replace('"','')
        value = self.__degeneralize_type(value_as_string)
        return(value)

    def __get_axis_index(self,line):
        key = line.split(' ')[0]
        number_as_string = key.split('-')[-1]
        number_as_int = int(number_as_string)
        return(number_as_int)

    def __get_axis_column(self,line):
        key = line.split(' ')[0]
        column_uppercase = key.replace(AXIS_DATA_INDICATOR,'')
        column_lowercase = column_uppercase.lower()
        return(column_lowercase)

    def __get_x(self, intline):
        x_as_string = intline.split(' ')[0]
        return(float(x_as_string))

    def __get_y(self, intline):
        y_as_string = intline.split(' ')[1]
        return(float(y_as_string))

    def __degeneralize_type(self,value_as_string):
        if value_as_string.isnumeric():
            value = int(value_as_string)
        else:
            try: 
                value = float(value_as_string)
            except ValueError:
                value = value_as_string
        return(value)

    def get_metadata_final(self):
        return(self.__metadata_raw)

    def get_axisdata_final(self):
        axisdata = self.__axisdata_raw.set_index('name',append=True).reset_index()
        return(axisdata)
    
    def get_intdata_final(self):
        xname = self.__metadata_raw[XAXIS_INDICATOR]
        yname = 'I'
        data_dict = {xname:self.__intdata_x,yname:self.__intdata_y}
        dataframe = pd.DataFrame(data_dict)
        scantype = self.__get_scan_type()
        if scantype == ScanTypes.SCAN2D:
            stepaxis = self._get_step_axis()
            step_position = self.__get_step_position()
            dataframe[stepaxis] = step_position
        return(dataframe)

    def __get_scan_type(self):
        if STEP_AXIS_INDICATOR in self.__metadata_raw:
            return(ScanTypes.SCAN2D)
        else:
            return(ScanTypes.SCAN1D)

    def __get_step_axis(self):
        return(self.__metadata_raw[STEP_AXIS_INDICATOR])

    def __get_step_position(self,step_axis):
        positions = self.__axisdata_raw['position']
        return(positions[self.__axisdata_raw['name'] == step_axis])