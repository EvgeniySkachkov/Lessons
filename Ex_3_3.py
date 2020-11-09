def my_func(a, b, c):
    if a == max(a, b, c):
        return a + max(b, c)
    elif b == max(b, c):
        return b + max(a, c)
    return c + max(a, b)


a, b, c = input("Введите числа: ").split(" ")
try:
    a, b, c = float(a), float(b), float(c)
    print(my_func(a, b, c))
except ValueError:
    print("Некорректные данные.")
