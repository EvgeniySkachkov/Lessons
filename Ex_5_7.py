import json


try:
    with open("Files/Ex_5_7_text.txt", "r") as file:
        profit = 0  # Прибыль фирмы
        c_profit = 0  # Средняя прибыль всех фирм, не имеющих убытков
        count = 0  # Количество фирм не имеющих убытков
        dict_profit = [{}, {}]  # Итоговый словарь для импорта в JSON

        for i, el in enumerate(file.readlines()):
            if int(el.split()[2]) - int(el.split()[3]) >= 0:
                print(f'Прибыль фирмы "{el.split()[1]} {el.split()[0]}" равна: {int(el.split()[2]) - int(el.split()[3])}')
                c_profit += (int(el.split()[2]) - int(el.split()[3]))
                dict_profit[0].update({el.split()[0]: (int(el.split()[2]) - int(el.split()[3]))})
                count += 1
            else:
                print(f'Убыток фирмы "{el.split()[1]} {el.split()[0]}" составил: {abs(int(el.split()[2]) - int(el.split()[3]))}')
        c_profit //= count
        print(f'Средняя прибыль компаний, не имеющих убытков, составила:  {c_profit}')
        dict_profit[1].update({'Средняя прибыль': c_profit})
        print(dict_profit)

        try:
            with open('Files/Ex_5_7.json', 'w') as file_2:
                json_obj = json.dumps(dict_profit, ensure_ascii=False)
                file_2.write(json_obj)
        except IOError:
            print("Не удалось открыть json файл.")

except IOError:
    print("Произошла ошибка открытия файла.")
