import os
import core.data_processor.file_reader as FR


def main():
    file_path = os.getcwd() + '/data_base/'
    worker = FR.file_reader(file_path)
    worker.read_files()
    data_frame = worker.data_frames_dict
    choice = None

    stages_and_frames = [['тип почвы', 'type_soil.xlsx', data_frame.get('type_soil.xlsx')],
                         ['подтип почвы', 'type_gran.xlsx', data_frame.get('type_gran.xlsx')],
                         ['сельскохозяйственная культура', 'spr_cul.xlsx', data_frame.get('spr_cul.xlsx')],
                         ['фаза роста', 'dan_cul.xlsx', data_frame.get('dan_cul.xlsx')]]

    variables_list = []
    # .name_poch
    # .name_mehs
    # .name_kul
    # .name_kul



if __name__ == '__main__':
    main()
