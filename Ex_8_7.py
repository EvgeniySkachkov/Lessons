class Complex_Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f'({self.a} - {self.b * -1}j)'
        else:
            return f'({self.a} + {self.b}j)'

    def __add__(self, other):
        return Complex_Number(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        Re = (self.a * other.a) - (self.b * other.b)
        Im = (self.a * other.b) + (self.b * other.a)
        return Complex_Number(Re, Im)


compl = Complex_Number(1, -1)
compl_1 = Complex_Number(3, 6)
compl_2 = Complex_Number(-5, 8)
print(f'{compl} + {compl_1} = {compl + compl_1}')
print(f'{compl_1} + {compl_2} = {compl_1 + compl_2}')
print(f'{compl} + {compl_1} + {compl_2}) = {compl + compl_1 + compl_2}\n')
print(f'{compl} * {compl_1} = {compl * compl_1}')
print(f'{compl_1} * {compl_2} = {compl_1 * compl_2}')
print(f'{compl} * {compl_1} * {compl_2}) = {compl * compl_1 * compl_2}')