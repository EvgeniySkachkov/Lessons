def my_func_1(x, y):
    return pow(x, y)


def my_func_2(x, y):
    temp = 1
    for _ in range(abs(y)):
        temp *= x
    return 1 / temp


x, y = input("Введите числа: ").split(" ")
try:
    x, y = float(x), int(y)
    y = abs(y) * -1  # Независимо от ввода, сделать Y отрицательным
    print(f"{my_func_1(x, y)} - способ с использованием внутренней функции.")
    print(f"{my_func_2(x, y)} - способ без использования внутренней функции.")
except ValueError:
    print("Некорректные данные.")
