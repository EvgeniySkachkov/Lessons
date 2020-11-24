def my_func(a, b, c):
    digits = [a, b, c]
    digits.sort(reverse=True)
    return digits[0] + digits[1]


a, b, c = input("Введите числа: ").split()
try:
    a, b, c = float(a), float(b), float(c)
    print(my_func(a, b, c))
except ValueError:
    print("Некорректные данные.")
