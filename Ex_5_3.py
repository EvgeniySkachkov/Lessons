try:
    with open('Files/Ex_5_3_text.txt', 'r') as file:
        profit = 0  # Общая прибыль сотрудников
        count = 0  # Количество сотрудников, с окладом более 20000

        print('Сотрудники, чьи оклады меньше 20000: ')
        for i, el in enumerate(file.readlines()):
            if int(el.split()[1]) < 20000:
                print(f'{el.split()[0]}')
            profit += int(el.split()[1])
            count += 1
        print(f'Средняя величина дохода сотрудников: {profit // count}')
except IOError:
    print("Произошла ошибка открытия файла.")
