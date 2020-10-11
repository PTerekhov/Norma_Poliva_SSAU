import os
import pandas as pd

class file_reader:
    def __init__(self, file_path):
        self.data_files_list = []
        self.data_frames_dict = {}
        self.FILE_PATH = file_path
        for (dirpath, dirnames, filenames) in os.walk(self.FILE_PATH):
            self.data_files_list.extend(filenames)
            break

    def read_files(self):
        for filename in self.data_files_list:
            file = self.FILE_PATH + filename
            self.data_frames_dict.update({filename: pd.read_excel(file, na_filter=False)})