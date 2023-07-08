# . Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple


Company = namedtuple("Company", "name, quarter1, quarter2, quarter3, quarter4, income")

companies = []
total_income = 0
n = int(input("Введите количество предприятий: "))
for _ in range(n):
    name = input("Введите наименование предприятия: ")
    q1 = float(input("Прибыль за первый квартал: "))
    q2 = float(input("Прибыль за второй квартал: "))
    q3 = float(input("Прибыль за третий квартал: "))
    q4 = float(input("Прибыль за четвёртый квартал: "))
    income = q1 + q2 + q3 + q4
    total_income += income
    companies.append(Company(name, q1, q2, q3, q4, income))

average_income = total_income / n

above_average = []
below_average = []
for company in companies:
    if company.income > average_income:
        above_average.append(company.name)
    else:
        below_average.append(company.name)

print(f'Предприятия с прибылью выше среднего: {", ".join(above_average)}')
print(f'Предприятия с прибылью ниже среднего: {", ".join(below_average)}')
