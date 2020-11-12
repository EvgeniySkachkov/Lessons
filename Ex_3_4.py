def my_func_2(x, y):
    temp = 1
    for _ in range(abs(y)):
        temp *= x
    return 1 / temp


x, y = input("Введите числа: ").split(" ")
try:
    x, y = float(x), int(y)
    y = abs(y) * -1  # Независимо от ввода, сделать Y отрицательным
    print(f"{my_func_2(x, y)}")
except ValueError:
    print("Некорректные данные.")
