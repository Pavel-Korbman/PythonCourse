# РАБОТА С ФАЙЛАМИ
# Задача №49
'''
Создать телефонный справочник
с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона
- данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик
для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''
# МОЁ РЕШЕНИЕ
'''
БД:
поле    тип    длинна    коммент
id      int      4       идентификатор записи
tel     string   24      номер телефона
family  string   100     фамилия
name    string   100     Имя
m_name  string   100     Отчество
'''


def add_tel():
    next_add = 'yes'
    data = open('phone_book_1.txt', 'a')
    while next_add == 'yes':
        telephone = input('Введите номер телефона (только цифры без пробелов): ')
        name = input('Введите ФИО латинскими буквами через пробел: ')
        next_add = input('Введите "yes" если хотите продолжить ввод. Любой другой символ, если нет :').lower()
        data.write(F' {name} {telephone} \n')
    data.close()
    print('Телефоны добавлены в телефонную книгу')


def print_tel():
    lst = open('phone_book_1.txt', 'r')
    for el in lst:
        print(el)
    lst.close()


def search_tel():
    word = input('Поиск по имени или телефону: ')
    a = False
    lst = open('phone_book_1.txt', 'r')
    for el in lst:
        if word in el:
            print(el)
            a = True
    lst.close()
    if a == False:
        print('Не найдено')


menu = input(
    'Введите "All" для просмотра всей книги.' 
    'Введите "Search" для поиска.' 
    'Введите "Add" для добавления новых записей: ').lower()
if menu == 'all':
    print_tel()
elif menu == 'search':
    search_tel()
elif menu == 'add':
    add_tel()
else:
    print('Не корректно')


'''
 Korbman Pavel Alex 89779225100

 Bezrukova Elena Vict 79779225050

 Ivanova Elena Vict 79779225051

 Ivaner Pavel Alegovic 89779225111 
'''

# СЕМИНАРСКОЕ РЕШЕНИЕ
