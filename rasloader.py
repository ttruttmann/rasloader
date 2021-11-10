from numpy import *
from .rasloader_helper import *

class RasLoader:
    def __init__(self, filename):
        self.append_file_inline(filename)

    def append_file_inline(self, filename):
        f = open(filename, 'r')
        self.__ensure_nextline_equals(f, START_RAS_LINE)
        while True:
            line = f.readline()
            if line == START_HEADER_LINE:
                header_lines = self.__extract_header_lines(f)
            elif line == START_INT_LINE:
                int_lines = self.__extract_int_lines(f)
                header_int_pair = HeaderIntPair(header_lines, int_lines)
                header_lines = None
                int_lines = None
                self.__absorb_header_int_pair(header_int_pair)
            elif line == END_RAS_LINE:
                self.__ensure_nextline_equals(f, END_FILE_LINE)
                self.__ensure_nextline_equals(f, '')
                f.close()
                break

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

    # TODO: Probably split this into smaller methods.
    def __absorb_header_int_pair(self, new_pair):
        if not hasattr(self, 'metadata'):
            self.metadata = new_pair.get_metadata_final()
        else:
            for new_key, new_value in new_pair.get_metadata_final().items():
                if new_key not in self.metadata:
                    continue
                elif self.metadata[new_key] != new_value:
                    self.metadata.pop(new_key)
        if not hasattr(self, 'axisdata'):
            self.axisdata = new_pair.get_axisdata_final()
        else:
            for i, row in new_pair.get_axisdata_final().iterrows():
                if self.axisdata.loc[i]['position'] != row['position']:
                    self.axisdata.loc[i]['position'] = NAN
        if not hasattr(self, 'intdata'):
            self.intdata = new_pair.get_intdata_final()
        else:
            self.intdata = self.intdata.append(new_pair.get_intdata_final(),ignore_index=True)

    def __ensure_nextline_equals(self, file, desired_line):
        if file.readline() != desired_line:
            raise UnexpectedLineException
