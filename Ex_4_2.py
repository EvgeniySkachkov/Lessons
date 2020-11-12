from random import randint

num = [randint(1, 50) for el in range(10)]
new_num = [num[i] for i in range(1, len(num)) if num[i] > num[i-1]]
print(num)
print(new_num)
