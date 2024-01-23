# Задача №39
'''
Даны два массива чисел.
Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве.
Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве.
Затем элементы второго массива
Ввод: 7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод:  3 3 2 12    (каждое число вводится с новой строки)
'''

# МОЁ РЕШЕНИЕ
'''
def fill_list():
    n = int(input('Введите количество элементов списка:'))
    lst = []
    for i in range(n):
        lst.append(int(input(f'Введите {i} элемент списка:')))
    return lst


list_1 = fill_list()
list_2 = fill_list()
for i in range(len(list_1)):
    if list_1[i] not in list_2:
        print(list_1[i])

# print(*list_1.[i])
# print(*list_2)
'''

# СЕМИНАРСКОЕ РЕШЕНИЕ вар 1
'''
list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
lst_res = []
for el in list_1:
    if el not in list_2:
        lst_res.append(el)
print(lst_res)

# СЕМИНАРСКОЕ РЕШЕНИЕ вар 2
print([el for el in list_1 if el not in list_2]) # Через генератор списков
'''

# О ГЕНЕРАТОРАХ (ВКЛЮЧЕНИЯХ)
# Создаём множества
'''
set_1 = {1, 2, 3}
set_2 = set()
for el in set_1:
    set_2.add(el ** 2)
print(set_2)
print(type(set_2))

set_2 = set(el ** 2 for el in set_1) # Через генератор множеств (множественное включение) с функцией set
print(set_2)
print(type(set_2))

set_2 = {el ** 2 for el in set_1} # Через генератор множеств (множественное включение) с функцией set
print(set_2)
print(type(set_2))
'''
# Создаём словари
'''
dict_1 = {1: 'один', 2: 'два', 3: 'три'}
dict_2 = {}

for el, val in dict_1.items():
    dict_2[el] = val
print(dict_2)

dict_2 = {el: val for el, val in dict_1.items()}  # Через генератор словарей (словарное включение)
print(dict_2)
'''

# Задача №41
'''
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве  
Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел. 
Ввод: 5
1 2 3 4 5

Вывод:  0

Ввод: 5
1 5 1 5 1

Вывод:  2
'''

# МОЁ РЕШЕНИЕ
'''
def fill_list():
    n = int(input('Введите количество элементов списка:'))
    lst = []
    for i in range(n):
        lst.append(int(input(f'Введите {i} элемент списка:')))
    return lst


lst_1 = fill_list()
# lst_1 = [1,2,3,4,5]
res = 0
for i in range(1, len(lst_1) - 1):
    if lst_1[i] > lst_1[i-1] and lst_1[i] > lst_1[i+1]:
        res += 1
print(res)
'''

# СЕМЕНАРСКОЕ РЕШЕНИЕ

# my_lst = list(map(int, input('Введите числа через пробел: ').split())) # Заполнение списка через функцию map().  map() - применяет любую функцию к каждому элементу последовательности. Делает объект map -
'''
lst = [1, 6, 3, 6, 5, 1]
count = 0
for i in range(1, len(lst) - 1):
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        count += 1
print(count)
'''
# Задача №43
'''
Дан список чисел. 
Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках. 
Ввод: 1 2 3 2 3
Вывод:  2
'''
'''
lst = [1, 2, 3, 2, 3, 3, 3, 3, 3, 3]
numbers = set(lst)
res = []
for el in numbers:
    if el in lst:
        res.append(lst.count(el) // 2)  # Функция .count(el) - частота вхождения (сколько раз элемент встречается в списке)
print(sum(res))
'''

# Задача №45
'''
Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает на вход одно натуральное число k, не превосходящее 105. 
Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. 
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод: 300
Вывод: 220 284
'''


# n = int(input('Введите число N:'))
# m = input('Введите число M:')
# k = int(input('Введите число K:'))


def get_sum(n):
    summ = 0
    for el in range(1, n):
        if n % el == 0:
            summ += el
    return summ


def get_friendly(k):
    res = []
    for n in range(1, k + 1):
        if n not in res:
            m = get_sum(n)
            if n == get_sum(m) and n != m:
                res.append(n)
                res.append(m)
    return res


print(*get_friendly(300))

# ДОМАШКА:

# Задача №1
'''
Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементами list_1 
и границы диапазона в виде чисел min_number, max_number.
На входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
На выходе:
1
2
3
6
7
9
10
11
13
14
16
19
'''
'''
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

for i in range(len(list_1)):
    if list_1[i] <= max_number and list_1[i] >= min_number:
        print(i)
'''

# Задача №2
'''
Заполните массив элементами арифметической прогрессии. 
Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

На входе:
a1 = 2
d = 3
n = 4
На выходе:
2
5
8
11
'''
'''
a1 = 2
d = 3
n = 4
a = [a1 + (i-1) * d for i in range(1, n+1)]
for el in a:
    print(el)
'''
