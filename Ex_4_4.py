list_ = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = (el for i, el in enumerate(list_) if list_.count(el) == 1)
print(list_)
print(tuple(new_list))
