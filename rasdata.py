from rasdata_helper import *

class RasData:
    def __init__(self, filename):
        self.scantype = ScanTypes.SCAN1D
        self.scantype = self.__determine_scantype(filename)
        if self.scantype == ScanTypes.SCAN1D: self.__parse1Dras(filename)
        elif self.scantype == ScanTypes.SCAN2D: self.__parse2Dras(filename)
    
    def __determine_scantype(self, filename):
        f = open(filename,'r')
        for line in f:
            if line.split(' ')[0] == "*MEAS_3DE_STEP_AXIS_INTERNAL":
                return(ScanTypes.SCAN2D)
        return(ScanTypes.SCAN1D)
    
    def __parse1Dras(self, filename):
        f = open(filename,'r')
        for line in f:
            line = line.replace('\n','')
            if line in LINES_TO_SKIP: continue
            elif line in LINES_TO_END: break
            elif "*MEAS_COND_AXIS_" in line:
                self.__parse_line_axis(line)
            elif '*' == line[0]:
                self.__parse_line_metadata(line)
            elif line[0] in ['-.0123456789']:
                self.__parse_line_data1D(line)
            else:
                raise UnexpectedLineException
    
    def __parse2Dras(self, filename):
        f = open(filename,'r')
        for line in f:
            line = line.replace('\n','')
            if line in LINES_TO_SKIP: continue
            elif line in LINES_TO_END: break
            elif line.split(' ')[0] == "*MEAS_3DE_STEP_AXIS_INTERNAL":
                step_axis = line.split(' ')[1].reaplace('"','')
            elif "*MEAS_COND_AXIS_" in line:
                self.__parse_line_axis(line)
            elif '*' == line[0]:
                self.__parse_line_metadata(line)
            elif line[0] in ['-.0123456789']:
                self.__parse_line_data2D(line)
            else:
                raise UnexpectedLineException

    def __parse_line_metadata(self, line):
        raise CodeNotCompleteException

    def __parse_line_axis(self, line):
        raise CodeNotCompleteException
    
    def __parse_line_data1D(self, line):
        raise CodeNotCompleteException
    
    def __parse_line_data2D(self, line, step_axis_value):
        raise CodeNotCompleteException

    def append_file(filename):
        raise CodeNotCompleteException