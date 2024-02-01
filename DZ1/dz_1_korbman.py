# ДОМАШНЕЕ ЗАДАНИЕ

'''
Дополнить справочник возможностью копирования данных из одного файла в другой.
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
'''

from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'
# file_name = 'phone_1.csv'

def get_user_data():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone_number = int(input('Введите телефон: '))
    return first_name, last_name, phone_number

def create_file(file_name):
    with open(file_name, 'w', encoding='UTF-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()





def read_file(file_name):
    with open(file_name, encoding='UTF-8') as data:  # Без режима т.к. по дефолту - чтение файла r
        f_reader = DictReader(data) # Читаем файл
        return list(f_reader)  # Возвращаем в виде списка



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


def copy_file(file_name, file_2, row_number):
    user_data = read_file(file_2)[row_number - 1]
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == user_data['Телефон']:
            print('Такой телефон уже существует')
            return
    obj = {'Имя': user_data['Имя'], 'Фамилия': user_data['Фамилия'], 'Телефон': user_data['Телефон']}
    res.append(obj)
    with open(file_name, 'w', encoding='UTF-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)
    print('Строка скопированна')



def main():
    while True:   # while True: - Бесконечный цикл (останавливается по команде
        command = input('Введите команду (w - создать, c - копировать из файла, r - читать, q - выйти): ')
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
        elif command == 'c':
            file_2 = input('Из какого файла копировать: ')
            row_number = int(input('Номер копируемой строки: '))
            if not exists(file_2):
                print('Файл источника не найден.')
                continue
            copy_file(file_name, file_2, row_number)
           # print('Строка скопированна')



main()














