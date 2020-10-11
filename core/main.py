import os
import re
import core.data_processor.file_reader as FR


def main():
    file_path = os.getcwd() + '/data_base/'
    file_worker = FR.file_reader(file_path)
    file_worker.read_files()
    data_frame = file_worker.data_frames_dict
    new_data_frames_list = []

    stages_and_frames = [['тип почвы', 'type_soil.xlsx', 'name_poch', 'code_meh'],
                         ['подтип почвы', 'type_gran.xlsx', 'name_meh', 'code_meh'],
                         ['сельскохозяйственная культура', 'spr_cul.xlsx', 'name_kul', 'code_kul'],
                         ['фаза роста', 'dan_cul.xlsx', 'name_faz', 'code_kul']]

    menu(stages_and_frames, data_frame, 0, new_data_frames_list)

def menu(stages, data_frame, i, new_data_frames_list):
    if i < 0:
        return 0
    elif i >= len(stages):
        return calculate(data_frame,new_data_frames_list)
    else:
        print('Выберите: ', stages[i][0])
        menu_item = data_frame.get(stages[i][1])
        needed_column = stages[i][2]
        if not new_data_frames_list:
            print(menu_item[needed_column])


        else:
            flag_column = stages[i][3]
            if flag_column in new_data_frames_list[i - 1].columns:
                flag_variables_list = list(re.findall(r'\d+', str(new_data_frames_list[i - 1][flag_column])))
                flag_variables_list.remove(flag_variables_list[0])
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


def calculate(data_frame1, data_frame2):
    print('Рассчет поливной нормы')

    temp_data_frame = data_frame1.get('dan_soil.xlsx')
    parameters = [data_frame2[0]['code_poch'], data_frame2[1]['code_meh']]
    columns1 = ['ob_massa', 'code_poch', 'code_meh']
    columns2 = ['wl_min', 'code_poch', 'code_meh']

    Max = data_frame2[3]['max_norma']
    H = data_frame2[3]['h_slo']
    Porog_NW = data_frame2[3]['porog_nw']
    RO = average(temp_data_frame, parameters, columns1)
    NW = average(temp_data_frame, parameters, columns2)
    P = 0.01 * (NW - Porog_NW)
    m = H * RO * NW * (1 - 0.01 * Porog_NW)

    print('MAX: ', float(Max))
    print('H: ', float(H))
    print('Porog_Nw: ', float(Porog_NW))
    print('RO: ', float(RO))
    print('NW: ', float(NW))
    print('P: ', float(P))
    print('m: ', float(m))

    return 0

def average(data_frame, parameters_list, columns):
    result = 0
    var = data_frame.loc[data_frame[columns[1]].isin(parameters_list[0]) &
                         data_frame[columns[2]].isin(parameters_list[1])]

    for element in var[columns[0]]:
       result += element

    return result/len(var)


if __name__ == '__main__':
    main()