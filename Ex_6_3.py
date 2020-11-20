class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {
        "wage": 0,
        "bonus": 0,
    }

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return f'Работнка зовут {self.surname} {self.name}'

    def get_total_income(self):
        return f'Доход сотрудника составляет {self._income["wage"] + self._income["bonus"]}'


person_1 = Position('Иван', 'Иванов', 'техник', 18600, 22400)
print(person_1.get_full_name())
print(person_1.get_total_income())

person_2 = Position('Сергей', 'Сергеев', 'уборщик', 7500, 2700)
print(person_2.get_full_name())
print(person_2.get_total_income())
