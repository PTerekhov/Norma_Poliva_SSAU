import os
import core.data_processor.file_reader as FR


def main():
    file_path = os.getcwd() + '/data_base/'
    worker = FR.file_reader(file_path)
    worker.read_files()
    data_frame = worker.data_frames_dict

    variables_list = []
    stages_and_frames = [['тип почвы', 'type_soil.xlsx', 'name_poch', 'mas_meh'],
                         ['подтип почвы', 'type_gran.xlsx', 'code_meh', 'name_mehs'],
                         ['сельскохозяйственная культура', 'spr_cul.xlsx', 'name_kul'],
                         ['фаза роста', 'dan_cul.xlsx', 'name_faz']]

    # choice = None
    # print('Выберите тип почвы')
    # print(data_frame.get(stages_and_frames[0][1]).name_poch)
    i = 0
    menu(stages_and_frames, data_frame, i, variables_list)


def menu(stages, data_frame, i, variables_list):
    if i < 0:
        return 0
    elif i >= len(stages):
        return variables_list
    else:
        breaker = 0
        print('Выберите ', stages[i][0])
        for column in data_frame.get(stages[i][1]).columns:
            if column in stages[i]:
                breaker += 1
                print(data_frame.get(stages[i][1])[column])
            if breaker != 0:
                break
        choice = input(':>> ')
        if choice.isnumeric():
            if 0 <= int(choice) <= len(data_frame.get(stages[i][1])):
                for index, row in data_frame.get(stages[i][1]).iterrows():
                    if index == int(choice):
                        needed_row = data_frame.get(stages[i][1]).iloc[index]
                        variables_list.append(needed_row)
                        i += 1
                        print('Выбрано: ')
                        for variable in variables_list:
                            print(variable)
                        print('\n\n\n\n')

                        menu(stages, data_frame, i, variables_list)
            else:
                print('Ошибка: такого варианта нет')
                print('\n\n\n\n')
                menu(stages, data_frame, i, variables_list)
        elif choice.lower() == 'q':
            return 0
        elif choice.lower() == 'b':
            print('\n\n\n\n')
            if variables_list:
                variables_list.pop(i-1)
            else:
                return 0
            menu(stages, data_frame, i - 1, variables_list)


if __name__ == '__main__':
    main()
