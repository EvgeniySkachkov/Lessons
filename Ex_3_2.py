def person(name, second_name, b_date, city, email, phone):
    return name, second_name, b_date, city, email, phone


name_ = input("Введите имя: ")
second_name_ = input("Введите фамилию: ")
b_date_ = input("Введите дату рождения: ")
city_ = input("Введите город проживания: ")
email_ = input("Введите Email: ")
phone_ = input("ВВведите номер телефона: ")
print(person(name=name_, second_name=second_name_, b_date=b_date_, city=city_, email=email_, phone=phone_))
