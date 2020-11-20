class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Отрисовка выполняется ручкой.'


class Pencil:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Отрисовка выполняется карандашом.'


class Handle:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Отрисовка выполняется маркером.'


stationery_1 = Pen('Ручка')
print(stationery_1.title)
print(stationery_1.draw())

stationery_2 = Pencil('Карандаш')
print(stationery_2.title)
print(stationery_2.draw())

stationery_3 = Handle('Маркер')
print(stationery_3.title)
print(stationery_3.draw())
