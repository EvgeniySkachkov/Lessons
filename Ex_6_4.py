class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула на {direction}'

    def showSpeed(self):
        return f'Текущая скорость автомобиля {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def showSpeed(self):
        if self.speed > 60:
            return f'Скорость автомобиля = {self.speed} км/ч. Автомобиль превысиль скорость.'
        return f'Скорость автомобиля = {self.speed} км/ч.'


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def showSpeed(self):
        if self.speed > 40:
            return f'Скорость автомобиля = {self.speed} км/ч. Автомобиль превысиль скорость.'
        return f'Скорость автомобиля = {self.speed} км/ч.'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


car_1 = SportCar('ford', 'белая', 50)
print(car_1.go())
print(car_1.turn("право"))
print(car_1.stop())
print(car_1.showSpeed())

car_2 = TownCar('toyota', 'желтая', 75)
print(car_2.go())
print(car_2.turn("лево"))
print(car_2.stop())
print(car_2.showSpeed())

car_3 = WorkCar('mazda', 'синяя', 35)
print(car_3.go())
print(car_3.turn("право"))
print(car_3.stop())
print(car_3.showSpeed())

car_4 = PoliceCar('bmw', 'черная', 45)
print(car_4.go())
print(car_4.turn("право"))
print(car_4.stop())
print(car_4.showSpeed())
