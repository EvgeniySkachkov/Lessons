def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Неверные аргументы."


var_1, var_2 = input("Введите числа: ").split(" ")
var_1, var_2 = float(var_1), float(var_2)
print(div(var_1, var_2))
