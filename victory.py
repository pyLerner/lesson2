dates_of_birth = {'П.Л. Чебышев': '16.05.1821',
                  'М.В. Ломоносов': '19.11.1711',
                  'Д.И. Менделеев': '8.11.1834',
                  'А.С. Попов': '16.03.1859',
                  'Н.И. Лобачевский': '01.12.1792'
                  }
rights = 0

while True:
    for scientist, date in dates_of_birth.items():
        answer = input(f'Дата рождения {scientist}?')
        if answer == dates_of_birth[scientist]:
            print('Верно')
            rights += 1
        else:
            print('Неверно')

    totals = rights / 5 * 100
    print(f'Процент правильных ответов: {totals}%')
    continue_desision = input('Повторить? [y/n]')

    if continue_desision == 'n':
        print('Ну как хотите. Выходим.')
        break
    else:
        print('\n\n')   # Отступ перед новой викториной


