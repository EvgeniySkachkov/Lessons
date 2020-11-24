class Cell:

    def __init__(self, count):
        self.count = count

    def make_order(self, n=5):
        a, b = divmod(self.count, n)
        nl = "\n"
        return f'{(("*" * n) + nl) * a}{"*" * b}{nl}'

    def __add__(self, other):
        print(f"{self.count} + {other.count}")
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count < 0:
            print("Разность клеток меньше нуля.")
            return Cell(0)
        else:
            print(f"{self.count} - {other.count}")
            return Cell(self.count - other.count)

    def __mul__(self, other):
        print(f"{self.count} * {other.count}")
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        print(f"{self.count} / {other.count}")
        return Cell(round(self.count / other.count))


c_1 = Cell(7)
c_2 = Cell(5)
print(c_1.make_order())
print(c_2.make_order())
print((c_1 + c_2).make_order(4))
print((c_1 - c_2).make_order(4))
print((c_2 - c_1).make_order(4))
print((c_1 * c_2).make_order(4))
print((c_1 / c_2).make_order(4))
print((c_2 / c_1).make_order(4))
