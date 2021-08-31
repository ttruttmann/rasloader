from rasloader_helper import *
import pandas as pd


class RasLoader:
    def __init__(self, filename):
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
        self.__ensure_nextline_equals(f,START_RAS_LINE)
        self.__verify_line_equals(f,START_HEADER_LINE)
        header_lines = self.__extract_header_lines(f)
        self.__verify_line_equals(f,START_INT_LINE)
        int_lines = self.__extract_int_lines(f)
        self.__ensure_nextline_equals(f,END_RAS_LINE)
        self.__ensure_nextline_equals(f,END_FILE_LINE)
        self.__ensure_nextline_equals(f,'')
        f.close()
        header_int_pair = HeaderIntPair(header_lines,int_lines)
        self.metadata = header_int_pair.get_final_metadata()
        self.axisdata = header_int_pair.get_final_axisdata()
        self.intdata  = header_int_pair.get_final_intdata()

    def __parse2Dras(self, filename):
        f = open(filename,'r')
        self.__ensure_nextline_equals(f,START_RAS_LINE)
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
                self.__ensure_nextline_equals(f,END_FILE_LINE)
                self.__ensure_nextline_equals(f,'')

    def __extract_header_lines(self, file):
        lines = []
        while True:
            next_line = file.readline()
            if next_line == END_HEADER_LINE:
                break
            else:
                lines.append(next_line)
        return(lines)

    def __extract_int_lines(self, file):
        lines = []
        while True:
            next_line = file.readline()
            if next_line == END_INT_LINE:
                break
            else:
                lines.append(next_line)
        return(lines)

    def __absorb_header_int_pair(self,header_int_pair):
        raise CodeNotCompleteException

    def __ensure_nextline_equals(self,file,desired_line):
        if file.getlines() != desired_line:
            raise UnexpectedLineException

    def append_file(filename):
        raise CodeNotCompleteException