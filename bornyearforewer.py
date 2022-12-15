# Проверка знания даты рождения Пушкина

date_of_birth = '06.06.1799'
date = date_of_birth[:-5]
year = date_of_birth[-4:]

while True:
    your_year = input('Год рождения Пушкина?\n')
    if your_year == year:
        break
    else:
        print('Неверный год')

while True:
    your_date = input('Дата рождения Пушкина? ')
    if your_date == date:
        print('Верно')
        break