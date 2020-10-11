import os
import re
import core.data_processor.file_reader as FR


def main():
    file_path = os.getcwd() + '/data_base/'
    file_worker = FR.file_reader(file_path)
    file_worker .read_files()
    data_frame = file_worker.data_frames_dict
    new_data_frames_list = []

    stages_and_frames = [['тип почвы', 'type_soil.xlsx', 'name_poch', 'code_meh'],
                         ['подтип почвы', 'type_gran.xlsx', 'name_meh', 'code_meh'],
                         ['сельскохозяйственная культура', 'spr_cul.xlsx', 'name_kul', 'code_kul'],
                         ['фаза роста', 'dan_cul.xlsx', 'name_faz', 'code_kul']]

    i = 0
    if menu(stages_and_frames, data_frame, i, new_data_frames_list) != 0:
        for element in new_data_frames_list:
            print(element)
    else:
        return 0


def menu(stages, data_frame, i, new_data_frames_list):
    if i < 0:
        return 0
    elif i >= len(stages):
        return new_data_frames_list
    else:
        print('Выберите ', stages[i][0])
        menu_item = data_frame.get(stages[i][1])
        needed_column = stages[i][2]
        if not new_data_frames_list:
            print(menu_item[needed_column])
        else:
            flag_column = stages[i][3]
            if flag_column in new_data_frames_list[i-1].columns:
                flag_variables_list = list(re.findall(r'\d+', str(new_data_frames_list[i - 1][flag_column])))
                if flag_variables_list:
                    menu_item = menu_item.loc[menu_item[flag_column].isin(flag_variables_list)]
            print(menu_item[needed_column])

        print('b: назад \nq: выход')
        choice = input(':>> ')
        if choice.isnumeric():
            if int(choice) in menu_item.index:
                new_data_frames_list.append(menu_item.loc[[int(choice)], :])
                print('Выбрано: ')
                for element in new_data_frames_list:
                    print(element)
                print('\n\n\n\n')
                i += 1
                menu(stages, data_frame, i, new_data_frames_list)
            else:
                print('Ошибка: такого варианта нет \n\n\n\n')
                menu(stages, data_frame, i, new_data_frames_list)
        elif choice.lower() == 'q':
            return 0
        elif choice.lower() == 'b':
            if new_data_frames_list:
                new_data_frames_list.pop(i - 1)
            else:
                return 0
            menu(stages, data_frame, i - 1, new_data_frames_list)
        else:
            print('Ошибка: такого варианта нет \n\n\n\n')
            menu(stages, data_frame, i, new_data_frames_list)


if __name__ == '__main__':
    main()
