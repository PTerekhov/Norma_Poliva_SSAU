import os
from os import walk


def main():
    data_files_list = []
    root_dir = os.getcwd()
    file_path = root_dir + '/data_base/'

    ### получаем список файлов в директории data_base
    for (dirpath, dirnames, filenames) in walk(file_path):
        data_files_list.extend(filenames)
        break
    print(data_files_list)


    


if __name__ == '__main__':
    main()
