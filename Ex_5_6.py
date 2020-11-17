try:
    with open('Files/Ex_5_6_text.txt', 'r+') as file:
        hours = 0  # Общее число часов по каждому предмету
        j = 1  # Счетчик
        flag = True
        dict_ = {}  # Итоговый словарь

        for i, el in enumerate(file.readlines()):
            while flag:  # Цикл для подсчета общего числа часов по каждому предмету
                try:
                    hours += int(el.split()[j].split('(')[0])
                    j += 1
                except IndexError:
                    flag = False
                dict_.update({el.split()[0][:-1]: hours})
            flag = True
            j = 1
            hours = 0
        file.seek(0)
        print(file.read())
        print(dict_)
except IOError:
    print("Произошла ошибка открытия файла.")
