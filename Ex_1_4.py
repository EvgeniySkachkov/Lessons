n = int(input("Введите положительное целое число:"))
if n < 0: n *= -1
max = 0
o = 0
while n != 0:
    (n,o) = divmod(n,10)
    if o > max:
        max = o
print(max)


