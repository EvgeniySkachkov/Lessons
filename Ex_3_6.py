def int_func(word_):
    return word_.title()


def int_func_2(string_):
    string_ = list(string_.split(" "))
    for i, el in enumerate(string_):
        string_[i] = int_func(el)
    string_ = ' '.join(string_)
    return string_


word = input("Введите слово: ")
print(int_func(word))
str_ = input("Введите несколько слов через пробел: ")
print(int_func_2(str_))
