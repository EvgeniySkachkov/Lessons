from abc import ABC
from abc import abstractmethod


class StorageTech:
    def __init__(self, name, address):
        self.name = name
        self.storageAddress = address
        self.accounting = {  # Словарь для учета техники для конкретного склада
            "Принтер": 0,
            "Кофеварка": 0,
            "Обогреватель": 0,
        }

    def __str__(self):
        return f'Название склада {self.name}\nСклад находится по адресу: {self.storageAddress}\n' \
               f'Наличие товара на складе на данный момент:' \
               f'\n\tПринтер - {self.accounting["Принтер"]} шт.' \
               f'\n\tКофеварка - {self.accounting["Кофеварка"]} шт.' \
               f'\n\tОбогреватель - {self.accounting["Обогреватель"]} шт.\n'


class OfficeEquipment(ABC):
    def __init__(self, count):
        self.count = count

    @abstractmethod
    def addToStorage(cls, NewStorage):
        pass


class Printer(OfficeEquipment):
    def __init__(self, count, type='лазерный'):
            count = int(count)
            super().__init__(count)
            self.type = type

    @classmethod
    def addToStorage(cls, NewStorage):  # Прием техники на склад
        count, type = input("Введите данные о товаре через пробел(Количество, тип(струйный, лазерный)):").split()
        while not is_int(count) or is_int(type):
            count, type = input("Неверные данные, попробуйте еще раз.\n").split()
        count = int(count)
        NewStorage.accounting["Принтер"] += count
        return Printer(count, type)

    @classmethod
    def transportToNewStorage(cls, OldStorage, NewStorage):  # Перемещение техники с одного склада на другой
        if OldStorage.accounting["Принтер"] == 0:
            print("На складе отсутствует данный товар. Перемещение с него невозможно.")
        else:
            print("Какое количество товара хотите переместить:")
            count = check_value(input())
            if OldStorage.accounting["Принтер"] >= count:
                OldStorage.accounting["Принтер"] -= count
                NewStorage.accounting["Принтер"] += count
            else:
                print('На складе нет данного количества товара.')


class CoffeeMachine(OfficeEquipment):

    def __init__(self, cost, volume=450):
        super().__init__(cost)
        self.volume = volume

    @classmethod
    def addToStorage(cls, NewStorage):  # Прием техники на склад
        count, volume = input("Введите данные о товаре через пробел(Количество, объём):").split()
        while not is_int(count) or not is_int(volume):
            count, volume = input("Неверные данные, попробуйте еще раз.\n").split()
        count = int(count)
        volume = int(volume)
        NewStorage.accounting["Кофеварка"] += count
        return CoffeeMachine(count, volume)

    @classmethod
    def transportToNewStorage(cls, OldStorage, NewStorage):  # Перемещение техники с одного склада на другой
        if OldStorage.accounting["Кофеварка"] == 0:
            print("На складе отсутствует данный товар. Перемещение с него невозможно.")
        else:
            print("Какое количество товара хотите переместить:")
            count = check_value(input())
            if OldStorage.accounting["Кофеварка"] >= count:
                OldStorage.accounting["Кофеварка"] -= count
                NewStorage.accounting["Кофеварка"] += count
            else:
                print('На складе нет данного количества товара.')


class Heater(OfficeEquipment):

    def __init__(self, cost, max_temperature=40):
        super().__init__(cost)
        self.max_temperature = max_temperature

    @classmethod
    def addToStorage(cls, NewStorage):  # Прием техники на склад
        count, max_temperature = input("Введите данные о товаре через пробел(Количество, максимальная температура нагрева):").split()
        while not is_int(count) or not is_int(max_temperature):
            count, max_temperature = input("Неверные данные, попробуйте еще раз.\n").split()
        count = int(count)
        max_temperature = int(max_temperature)
        NewStorage.accounting["Обогреватель"] += count

    @classmethod
    def transportToNewStorage(cls, OldStorage, NewStorage):  # Перемещение техники с одного склада на другой
        if OldStorage.accounting["Обогреватель"] == 0:
            print("На складе отсутствует данный товар. Перемещение с него невозможно.")
        else:
            print("Какое количество товара хотите переместить:")
            count = check_value(input())
            if OldStorage.accounting["Обогреватель"] >= count:
                OldStorage.accounting["Обогреватель"] -= count
                NewStorage.accounting["Обогреватель"] += count
            else:
                print('На складе нет данного количества товара.')


def is_int(num):
    try:
        num = int(num)
    except ValueError:
        return False
    return True


def check_value(value):
    while not is_int(value):
        value = input()
    value = int(value)
    return value


s_1 = StorageTech("Центральный склад", "ул. Ленина д.25 корп.1")
s_2 = StorageTech("Распределительный центр", "пр-кт Мира д.3")

while True:
    print('\nВыберите пункт меню, введя его номер:\n'
          '1: Просмотр доступных складов.\n'
          '2: Добавить товар на склад.\n'
          '3: Переместить товар на другой склад.\n'
          '4: Выход\n')
    v = check_value(input())  # Проверка на правильный ввод пункта меню
    if v == 4:  # Выход
        break

    if v == 1:  # Вывод данных о складах
        print(s_1)
        print(s_2)

    elif v == 2:  # Добавить товар на склад
        print(f'На какой склад добавить товар:\n'
              f'1: {s_1.name}.\n'
              f'2: {s_2.name}.\n'
              f'3: Выход.\n')
        v = check_value(input())
        print('\nВыберите пункт меню, введя его номер:\n'
              '1: Добавить принтеры.\n'
              '2: Добавить кофеварки.\n'
              '3: Добавить обогреватели.\n'
              '4: Назад в меню.\n')
        if v == 1:  # Добавить товар на 1-й склад
            v = check_value(input())
            if v == 1:
                Printer.addToStorage(s_1)
            elif v == 2:
                CoffeeMachine.addToStorage(s_1)
            elif v == 3:
                Heater.addToStorage(s_1)
        elif v == 2:  # Добавить товар на 2-ой склад
            v = check_value(input())
            if v == 1:
                Printer.addToStorage(s_2)
            elif v == 2:
                CoffeeMachine.addToStorage(s_2)
            elif v == 3:
                Heater.addToStorage(s_2)

    elif v == 3:  # Перемещение товара со склада на склад
        print('С какого склада хотите выполнить перемещение:\n'
              f'1: {s_1.name}\n'
              f'2: {s_2.name}\n'
              '3: Выход\n')
        v = check_value(input())
        print('\nВыберите пункт меню, введя его номер:\n'
              '1: Переместить принтеры.\n'
              '2: Переместить кофеварки.\n'
              '3: Переместить обогреватели.\n'
              '4: Выход.\n')
        if v == 1:   # Перемещение товара с 1-ого склада на 2-ой склад
            v = check_value(input())
            if v == 1:
                Printer.transportToNewStorage(s_1, s_2)
            elif v == 2:
                CoffeeMachine.transportToNewStorage(s_1, s_2)
            elif v == 3:
                Heater.transportToNewStorage(s_1, s_2)
        if v == 2:  # Перемещение товара со 2-ого склада на 1-ый склад
            v = check_value(input())
            if v == 1:
                Printer.transportToNewStorage(s_2, s_1)
            elif v == 2:
                CoffeeMachine.transportToNewStorage(s_2, s_1)
            elif v == 3:
                Heater.transportToNewStorage(s_2, s_1)


