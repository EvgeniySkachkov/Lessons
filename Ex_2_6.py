items = []

id = 0
name_ = ""
cost_ = 0
count_ = 0
ed_ = ""

analitics_ = {"название": [], "стоимость": [], "количество": [], "ед.": []}

n = int(input("введите количество товара: "))
i = 0
while i < n:
    name_ = input("Введите название товара: ")
    analitics_["название"].append(name_)
    cost_ = input("Введите стоимость товара: ")
    analitics_["стоимость"].append(cost_)
    count_ = input("Введите количество товара: ")
    analitics_["количество"].append(count_)
    ed_ = input("Введите единицу измерения: ")
    analitics_["ед."].append(ed_)
    items.append((id, {"название": name_, "стоимость": cost_, "количество": count_, "ед.": ed_}))
    id += 1
    i += 1

for id, item in enumerate(items):
    print(item)
print(analitics_)
