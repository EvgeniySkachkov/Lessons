def fact(num):
    i = 1
    for el in range(1, num + 1):
        i *= el
        yield i


n = 10
i = 1
for el in fact(n):
    print(f"{i:2}! =  {el}")
    i += 1
