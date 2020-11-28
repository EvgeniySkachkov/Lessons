class CheckListForNumErr(Exception):

    def __init__(self, text):
        self.text = text

    @staticmethod
    def check(num):
        try:
            num = int(num)
        except ValueError:
            return False
        else:
            return True


ls = []
while True:
    try:
        num = input("Введите число, чтобы завершить работу программы введите stop: ")
        if num == "stop":
            break
        if CheckListForNumErr.check(num):
            ls.append(int(num))
        else:
            raise CheckListForNumErr("Вы ввели неверные данные.")
    except CheckListForNumErr as e:
        print(e)
        
print(ls)