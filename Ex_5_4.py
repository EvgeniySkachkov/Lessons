try:
    with open('Files/Ex_5_4_text.txt', 'r') as file_1:
        with open('Files/Ex_5_4_text_2.txt', 'w+') as file_2:
            dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', }
            print(file_1.read())
            file_1.seek(0)
            for i, el in enumerate(file_1):
                file_2.write(el.replace(el.split()[0], dict[el.split()[0]]))
            file_2.seek(0)
            print(file_2.read())
except IOError:
    print("Произошла ошибка открытия файла.")
