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
        self.__verify_first_lines(f)
        self.__verify_line_equals(f,START_HEADER_LINE)
        header_lines = self.__extract_header_lines(f)
        self.__verify_lines_equals(f,START_INT_LINE)
        int_lines = self.__extract_int_lines(f)
        self.__ensure_nextline_equals(file,END_RAS_LINE)
        self.__verify_last_lines(f)
        f.close()
        header_int_pair = HeaderIntPair(header_lines,int_lines)
        self.metadata = header_int_pair.get_final_metadata()
        self.axisdata = header_int_pair.get_final_axisdata()
        self.intdata  = header_int_pair.get_final_intdata()

    def __parse2Dras(self, filename):
        f = open(filename,'r')
        self.__verify_first_lines(f)
        while True:
            line = f.readline()
            if line == START_HEADER_LINE:
                header_lines = self.__extract_header_lines(f)
            elif line == START_INT_LINE:
                int_lines = self.__extract_int_lines(f)
                header_int_pair = HeaderIntPair(header_lines,int_lines)
                int_lines = None
                header_lines = None
                self.__absorb_header_int_pair(header_int_pair)
            elif line == END_RAS_LINE:
                self.__verify_last_lines(f)

    def __parse_line_metadata(self, line):
        raise CodeNotCompleteException

    def __parse_line_axis(self, line):
        raise CodeNotCompleteException
    
    def __parse_line_data1D(self, line):
        raise CodeNotCompleteException
    
    def __parse_line_data2D(self, line, step_axis_value):
        raise CodeNotCompleteException
    
    def __verify_first_lines(self,file):
        self.__ensure_nextline_equals(file,START_RAS_LINE)

    def __verify_last_lines(self,file):
        self.__ensure_nextline_equals(file,END_FILE_LINE)
        self.__ensure_nextline_equals(file,'')

    def __ensure_nextline_equals(self,file,desired_line):
        if file.getlines() != desired_line:
            raise UnexpectedLineException

    def append_file(filename):
        raise CodeNotCompleteException