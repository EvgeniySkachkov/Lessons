import re


class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        out = ''
        for i, el in enumerate(list(self.matr)):
            for j, elem in enumerate(el):
                out = f'{out} {elem}  '
            print(out)
            out = ''
        return f''

    def get_matr_el(self, i, j):
        return self.matr[i][j]

    def __add__(self, other):
        new_matr = []
        for i, el in enumerate(self.matr):
            new_matr.append([])
            for j, elem in enumerate(el):
                new_matr[i].append(elem + other.get_matr_el(i, j))
        new_matr = Matrix(new_matr)
        return new_matr


m = [[1, 2], [3, 4], [5, 6]]
m_1 = [[1, 1], [1, 1], [1, 1]]
ex_1 = Matrix(m)
ex_2 = Matrix(m_1)
print(ex_1)
print(ex_2)
print(ex_1 + ex_2)
