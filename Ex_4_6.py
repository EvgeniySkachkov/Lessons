from itertools import count
from itertools import cycle

down_b = 1
up_b = 5
list_1 = []
for el in count(down_b):
    if el > up_b:
        break
    else:
        list_1.append(el)
print(list_1)

list_2 = []
i = 0
for el in cycle(list_1):
    if i > 10:
        break
    else:
        list_2.append(el)
        i += 1
print(list_2)
