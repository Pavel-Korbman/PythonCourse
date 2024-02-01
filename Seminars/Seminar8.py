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


# СЕМИНАРСКОЕ РЕШЕНИЕ

# Вызываем библиотеки, которые будем использовать
from csv import DictReader, DictWriter
'''
DictReader - для чтения - вернёт содержимое файла в виде списка словарей (построчно),
DictWriter - для записи - запишет список словарей в файл в виде строк
'''
from os.path import exists  #  exists - Проверяет есть ли файл. Если есть вернёт True, если нет - False

class NameError:  #  Создаём свой класс неправильного ввода имени (исключений)
    def __init__(self, txt):
        self.txt = txt
class PhoneError:
    def __init__(self, txt):
        self.txt = txt
def get_user_data():
    flag = False
    while not flag:   # Делаем валидацию телефона
        try:  # try: - Повторяем попытку
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Неправильная длинна')  #  raise NameError - Приминяем класс исключений
            last_name = input('Введите фамилию: ')
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) < 11:
                raise PhoneError('Не верная длинна номера')
        except ValueError:   # Печатаем если введены неправильные данные (встроенный класс определения непр. данных)
            print('Вы вводите символы вместо цифр!')
            continue
        except NameError as err:
            print(err)
            continue
        except PhoneError as err:
            print(err)
            continue

    return first_name, last_name, phone_number # Без скобок возвращает кортеж

def create_file(file_name):
    with open(file_name, 'w', encoding='UTF-8') as data:  # Блок работы с файлом. data - переменная для передачи данных
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон']) # Создаём заголовок полей
        f_writer.writeheader()    # .writeheader() - делает хэдер из переменной f_writer


file_name = 'phone.csv'
# create_file(file_name)     # Вызвали функцию и создали файл с шапкой

def read_file(file_name):
    with open(file_name, encoding='UTF-8') as data:  # Без режима т.к. по дефолту - чтение файла r
        f_reader = DictReader(data) # Читаем файл
        return list(f_reader)  # Возвращаем в виде списка


# print(read_file('phone.csv'))

def write_file(file_name):
    user_data = get_user_data()  # положили в переменную кортежи со строками справочника
    res = read_file(file_name)  # берём из файла список с данными
    for el in res:   # проверяем есть ли уже такой телефон
        if el['Телефон'] == str(user_data[2]):
            print('Такой телефон уже существует')
            return
    obj = {'Имя': user_data[0], 'Фамилия': user_data[1], 'Телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='UTF-8', newline='') as data:
        # Перезаписываем Хэдер и добавляем данные. newline='' чтобы не было пустых строк
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)  # writerows(res) - Добавляет строки


def main():
    while True:   # while True: - Бесконечный цикл (останавливается по команде
        command = input('Введите команду (w - создать, r - читать, q - выйти): ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
            print('Данные записаны')
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан. Создайте его')
                continue  # Перейти на новую итерацию в while
            print(read_file(file_name))

main()
















