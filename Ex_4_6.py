from itertools import count
from itertools import cycle

down_b = 1
up_b = 5
list_ = []
for el in count(down_b):
    if el > up_b:
        break
    else:
        list_.append(el)
print(list_)

list_2 = []
i = 0
for el in cycle(list_):
    if i > 10:
        break
    else:
        list_2.append(el)
        i += 1
print(list_2)
