rating = [8, 6, 5, 5, 1]
num = 1
while num > 0:
    num = int(input("Введите число (Введите число меньше 1, чтобы выйти): "))
    if num in rating:
        rating.insert(rating.index(num) + rating.count(num), num)
    else:
        rating.append(num)
        rating.sort(reverse=True)
    print(rating)




