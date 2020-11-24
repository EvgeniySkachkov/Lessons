class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc_mass(self, asf_mass, count_sm):
        return self._length * self._width * asf_mass * count_sm


asphalt = Road(5000, 20)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {asphalt.calc_mass(25, 5)} кг.')

asphalt_1 = Road(1000, 4)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {asphalt_1.calc_mass(25, 5)} кг.')
