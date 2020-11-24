from abc import ABC, abstractmethod


class Clothes:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 38:
            self.__size = 38
        elif size > 70:
            self.__size = 70
        else:
            self.__size = size

    def show_name(self):
        return self.name

    def show_size(self):
        return self.size

    def calc(self):
        return f'Расход ткани для создания пальто = {self.size/6.5 + 0.5:.2f}'


class Costume(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            self.__height = 150
        elif height > 210:
            self.__height = 210
        else:
            self.__height = height

    def show_name(self):
        return self.name

    def show_height(self):
        return self.height

    def calc(self):
        return f'Расход ткани для создания костюма = {2 * self.height + 0.3:.2f}'


c_1 = Coat("пальто", 65)
print(c_1.show_name())
print(c_1.show_size())
print(c_1.calc())

c_1 = Coat("пальто", 88)
print(c_1.show_name())
print(c_1.show_size())
print(c_1.calc())

c_2 = Costume("смокинг", 150)
print(c_2.show_name())
print(c_2.show_height())
print(c_2.calc())

c_2 = Costume("смокинг", 189)
print(c_2.show_name())
print(c_2.show_height())
print(c_2.calc())
