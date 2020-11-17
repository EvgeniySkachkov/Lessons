from random import randint

try:
    with open('Files/Ex_5_5_text.txt', 'w+') as file:
        sum = 0

        list_ = (randint(0, 10) for _ in range(10))
        for i, el in enumerate(list(list_)):
            file.write(str(el) + ' ')

        file.seek(0)
        list_ = file.read().split()
        print(list_)
        for i, el in enumerate(list_):
            if el != ' ':
                print(f'{sum} + {el} = {sum + int(el)}')
                sum += int(el)
        print(f'Сумма чисел = {sum}')
except IOError:
    print("Произошла ошибка открытия файла.")
