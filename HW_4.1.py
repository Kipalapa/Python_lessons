#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами


def general_salary():
    worke_time = float(input('Введите количество отработанных часов : '))
    salary_per_hour = float(input('Введите суммы оплаты труда за 1 час : '))
    bonus = float(input('Укажите размер премии - '))
    pay = worke_time * salary_per_hour
    return pay + bonus
print(f'Размер заработной платы составил: {general_salary() }')



