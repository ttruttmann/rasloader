from rasloader_helper import *

class RasLoader:
    def __init__(self, filename):
        self.append_file(filename)
        
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

    def __absorb_header_int_pair(self,new_pair): # TODO: Probably split this into smaller methods.
        if not hasattr(self,'metadata'):
            self.metadata = new_pair.get_metadata_final()
        else:
            for new_key, new_value in new_pair.get_metadata_final():
                if not self.metadata.has_key(new_key):
                    raise InconsistentHeaderException
                elif self.metadata[new_key] != new_value:
                    self.metadata.pop(new_key)
        if not hasattr(self,'axisdata'):
            self.axisdata = new_pair.get_axisdata_final()
        else:
            for i,row in new_pair.get_axisdata_final():
                if self.axisdata.iloc[i]['position'] != row['position']:
                    self.axisdata.iloc[i]['position'] = nan
        if not hasattr(self,'intdata'):
            self.intdata = new_pair.get_intdata_final()
        else:
            self.indata = self.intdata.append(new_pair.get_intdata_final())

    def __ensure_nextline_equals(self,file,desired_line):
        if file.getlines() != desired_line:
            raise UnexpectedLineException

    def append_file(self,filename):
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