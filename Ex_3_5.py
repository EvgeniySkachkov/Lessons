def sum_(list_):
    global g_sum, flag_
    for i, el in enumerate(list_):
        try:
            g_sum += float(el)
        except ValueError:
            flag_ = False # Прерывание цикла ввода чисел, если встретился специальный символ
            return g_sum
    return g_sum


g_sum = 0.0
flag_ = True
while flag_:
    seq = input("Введите числа через пробел: ").split(" ")
    print(f"Сумма чисел равна - {sum_(seq)}")
