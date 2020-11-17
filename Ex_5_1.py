try:
    with open('Files/Ex_5_1_text.txt', 'w+') as file:
        while True:
            text = input()
            if text == '':
                break
            file.write(f'{text}\n')
except IOError:
    print("Произошла ошибка открытия файла.")
