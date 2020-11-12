def person(name, second_name, b_date, city, email, phone):
    return f'{second_name} {name}\n' \
           f'Дата рождения: {b_date}\n' \
           f'Город: {city}\n' \
           f'Почта: {email}\n' \
           f'Телефон: {phone}\n' \


print(person(
    name=input("Введите имя: "),
    second_name=input("Введите фамилию: "),
    b_date=input("Введите дату рождения: "),
    city=input("Введите город: "),
    email=input("Введите почту: "),
    phone=input("Введите телефон: "),
))

