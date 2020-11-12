list_ = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []
new_list = [list_[i] for i in range(len(list_)) if list_[i] not in new_list]
print(list_)
print(new_list)
