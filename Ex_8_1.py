class CheckValidExcepction(Exception):
    pass

class Date:

    def __init__(self, date_):
        self.date_ = date_

    @classmethod
    def get_elem_date(cls, date):
        out = [int(el) for i, el in enumerate(date.split('-'))]
        return out

    @staticmethod
    def check_valid(date):
        try:
            if date[0] > 31 or date[0] < 1:
                raise CheckValidExcepction('Неверное число дня.')
            elif date[1] > 12 or date[1] < 1:
                raise CheckValidExcepction('Неверное число месяца.')
            elif date[2] > 2020 or date[2] < 1000:
                raise CheckValidExcepction('Неверное число года.')
            return "Проверка прошла успешно."
        except CheckValidExcepction:
            return date
        except TypeError:
            print('Введены неверные данные.')
            return date



d = Date('10-11-1987')
d_1 = Date('52-12-1685')

print(Date.get_elem_date(d.date_))
d.date_ = Date.get_elem_date(d.date_)
print(Date.check_valid(d.date_))

print(Date.get_elem_date(d_1.date_))
d_1.date_ = Date.get_elem_date(d_1.date_)
print(Date.check_valid(d_1.date_))

