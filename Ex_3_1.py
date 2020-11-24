def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Неверные аргументы."


var_1, var_2 = (int(digit) for digit in input("Введите два числа через пробел: ").split())
print(div(var_1, var_2))
