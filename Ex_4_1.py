from sys import argv

script_name, rate, work_time, premium = argv
try:
    print(f"Зароботная плата сотрудника составляет: {(float(rate) * float(work_time)) + float(premium)}")
except TypeError:
    print("Неверные данные.")

