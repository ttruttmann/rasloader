from rasloader_helper import *

class RasLoader:
    def __init__(self, filename):
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