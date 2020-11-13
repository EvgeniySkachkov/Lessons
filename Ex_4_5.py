from functools import reduce

list_ = [el for el in range(100, 1001) if el % 2 ==0]
print(list_)
multiply = (reduce(lambda prev_el, el: prev_el * el, list_))
print(multiply)
