class ZeroDivisionErr(Exception):
    pass


while True:
    try:
        a, b = map(int, input("Введите два числа, делимое и делитель, через пробел (Чтобы выйти введите первым числом 0): ").split())
        if a == 0:
            break
        if b == 0:
            raise ZeroDivisionErr
        print(f'{a} / {b} = {a / b:.3}')
    except ZeroDivisionErr:
        print("Введены неверные данные: Невозможно делить на 0.")
    except ValueError:
        print("Введены неверные данные.")
