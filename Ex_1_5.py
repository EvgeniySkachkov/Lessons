m_in = int(input("Введите доход фирмы: "))
m_out = int(input("Введите расходы фирмы: "))
if m_in > m_out:
    print("Ваша фирма работает на прибыль.")
    print(f"Рентабельность выручки составляет: {(m_in - m_out) / m_in}")
    p = int(input("Введите количество сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет: {int((m_in - m_out) / p)}")
elif m_out > m_in:
    print("Ваша фирма работает в убыток.")
elif m_out == m_in:
    print("Ваша фирма работает в ноль.")
