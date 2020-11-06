a = float(input("Введите результат первого дня: "))
b = float(input("Введите конечный результат: "))
count = 1
print(f"{count}-й день: {a:0.2} км")
while a < b:
    a = a * 1.1
    count += 1
    print(f"{count}-й день: {a:0.3} км")
print(f"На {count} день спортсмен достиг результата - не менее {b} км.")

