s = input("Введите строку: ")
s = s.split()
for num,el in enumerate(s):
    print(f"{num}: {el[:10]}")


