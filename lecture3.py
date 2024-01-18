# ФУНКЦИИ:
'''
Создать функцию, суммирующую все элементы от 1 до n
'''

# Печатает:
'''
def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


# sum_numbers(5)
m = int(input('Введите число:'))
sum_numbers(m)
'''
# Возвращает:
'''
def sum_numbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
'''
'''
m = int(input('Введите число:'))
print(sum_numbers(m))
# Hello
# 28
'''
'''
m = int(input('Введите число:'))
print(sum_numbers(m, 'Привет'))
# Привет
# 55
'''
# ФУНКЦИЯ с неограниченным количеством аргументов:
'''
Вводим буквы, получаем слово
'''
'''
def word(*letters):
    res = ''
    for i in letters:
    #for i in str(letters):
       res += str(i)
    return res

print(word('П','р', 'и', 'в', 'е', 'т'))
print(word(1, 2, 3,))  #
'''


# МОДУЛЬНОСТЬ: (создание функций  в отдельных файлах и их вызов из главного файла с программой):

# Создали файл (модуль) modul_1.py с функцией max_1(a, b) для нахождения большего числа.
# Импортируем модуль в этот (главный файл:






