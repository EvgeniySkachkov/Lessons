c = int(input("Выберите способ ввода значаений списка: \n(1): Ввести значения по очереди. \n(2): Ввести весь список целиком, разделяя элементы пробелами. \n"))
l = []
i = 0
if c == 1:
    n = int(input("Введите длину списка: "))
    while i < n:
        l.append(int(input()))
        i += 1
else:
    l = list(input().split())
i = 0
print(l)
while i < len(l) - 1:
    l[i], l[i+1] = l[i+1], l[i]
    i +=2
print(l)




