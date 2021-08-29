from rasdata_helper import *

class RasData:
    def __init__(self, filename):
        self.scantype = ScanTypes.SCAN1D
        self.scantype = self.__determine_scantype(filename)
        if self.scantype == ScanTypes.SCAN1D: self.__parse1Dras(filename)
        elif self.scantype == ScanTypes.SCAN2D: self.__parse2Dras(filename)
    
    def __determine_scantype(self, filename):
        raise CodeNotCompleteError
    
    def __parse1Dras(self, filename):
        raise CodeNotCompleteError
    
    def __parse2Dras(self, filename):
        raise CodeNotCompleteError

    def __parse_line_metadata(self, line):
        raise CodeNotCompleteError

    def __parse_line_axis(self, line):
        raise CodeNotCompleteError
    
    def __parse_line_data1D(self, line):
        raise CodeNotCompleteError
    
    def __parse_linedata2D(self, line, step_axis_value):
        raise CodeNotCompleteError

    def append_file(filename):
        raise CodeNotCompleteError