def capitalize_func(text):
    def int_func(word: str):
        return f"{word[0].upper()}{word[1:]}"
    words = text.split()
    return ' '.join(list(map(lambda word: int_func(word), words)))


word = input("Введите слово: ")
print(capitalize_func(word))
str_ = input("Введите несколько слов через пробел: ")
print(capitalize_func(str_))
