try:
    with open('Files/Ex_5_2_text.txt', 'r') as file:
        content = file.readlines()

        print(f'Количество строк в файле: {len(content)}')
        for el in content:
            print(f"{el.rstrip()} - Количество слов в строке {el.count(' ') + 1}")
except IOError:
    print("Произошла ошибка открытия файла.")
