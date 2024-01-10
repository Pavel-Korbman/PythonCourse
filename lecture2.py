# СПИСКИ
"""
list_1 = []  # Пустой
list_2 = list()  # Пустой
"""
# list_1 = [3, 5, 1, 2, 8]
# print(list_1)  # Печать в кв скобках с запятыми
# print(*list_1)  # Печать в строку (без кв скобок и запятых)
# Печать в цикле в столбик:
"""
for i in list_1:
    print (i)
"""
# print(list_1[2])  # Печать третьего (с индексом 2) элемента

# Длинна списка len
# print(len(list_1))

# ЗАПОЛНЕНИЕ СПИСКА
"""
list_1 = [1, 5]
print(list_1)
list_1.append(20)
print(list_1)
"""
# Заполним список рядом от 0 до 4 :
"""
list_2 = []
for i in range(5):
    list_2.append(i)
print(*list_2)
# Заполним список рядом от 1 до 5 :
list_2 = []
for i in range(5):
    list_2.append(i+1)
    print(*list_2)  # Выводим каждый проход списка
#print(*list_2)
"""
# ФУНКЦИИ СПИСКОВ

# Удаление последнего элемента
"""
list_1 = [1, 2, 3, 4, 5]
print(*list_1)
print(list_1.pop())  # Печать удалённого элемента - 5
print(*list_1)  # 1 2 3 4
list_1.pop()
print(*list_1)  # 1 2 3
a = list_1.pop()
print(a)  # 3
print(*list_1)  # 1 2 
"""
# Удаление определённого элемента по индексу .pop(i), i-индекс элемента
"""
list_1 = [1, 2, 3, 4, 5]
print(*list_1)  # 1 2 3 4 5
print(list_1.pop(2))  # Печать удалённого элемента - 3
print(*list_1)  # 1 2 4 5
list_1.pop(0)
print(*list_1)  # 2 4 5
a = list_1.pop(1)
print(a)  # 4
print(*list_1)  # 2 5
"""
# Добавление элемента по индексу .insert(i, j), i-индекс элемента j-значение элемента
"""
list_1 = [1, 2, 3, 4, -5]
print(*list_1)  # 1 2 3 4 -5
print(list_1.insert(2, 33))  #Элемент вставлен, на печати None
print(*list_1)  # 1 2 33 3 4 -5
list_1.insert(0, -94)
print(*list_1)  # -94 1 2 33 3 4 -5

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*list_1)  # 1 2 3 4 5 6 7 8 9 10
print(list_1[len(list_1) - 1])  # 10
print(list_1[-1])  # 10
print(list_1[-2])  # 9
print(*list_1[:])  # 1 2 3 4 5 6 7 8 9 10
print(*list_1[2:])  # 3 4 5 6 7 8 9 10
print(*list_1[:2])  # 1 2
print(*list_1[1:9])  # 1 3 4 5 6 7 8 9
print(*list_1[1:9:2]) # 2 4 6 8 (с шагом 2)
print(*list_1[::3])  # 1 4 7 10 (с начала до конца с шагом 3)
"""

# КОРТЕЖИ
"""
t = ()
print(type(t))  # class 'tuple'
t = (1)
print(type(t))  # class 'int' - не кортеж
t = (1,)
print(type(t))  # class 'tuple' - кортеж

v = [1, 8, 9]
print(type(v))  # class 'list'
v = tuple(v)
print(type(v))  # class 'tuple'
print(v)  # (1, 8, 9)
print(*v)  # 1 8 9

v = (1, 8, 9)
a,b,c = v  # Разъединили на переменные
print(b)  # 8
d = v[2]
print(d)  # 9

t = (1, 2, 3, 5)

for i in t:
    print(i)              # Элементы в столбик

print(type(t))
for i in range(len(t)):
    print(t[i])           # Элементы в столбик
"""

# СЛОВАРИ
"""
dictionary_1 = {}
d = dict()
print(type(dictionary_1))  # class 'dict'
print(type(d))             # class 'dict'

d['q'] = 'QWERTY'
d['q1'] = 'QWERTYU'
print(d['q'], d['q1'])  # QWERTY QWERTYU
print(d)                # {'q': 'QWERTY', 'q1': 'QWERTYU'}
"""

#dictionary = {}
#dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}


# print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['down'])  # ↓

# # Добавление элемента:
"""
print(dictionary)
dictionary[88] = 880
print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 88: 880}
"""
# # Удаление элемента:
"""
del dictionary[88]
print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
"""
# # Печать в цикле:
"""
for i in dictionary:
    print(i, dictionary[i])
"""
"""
up ↑
left ←
down ↓
right →
"""
"""
for i in dictionary:
    print('{}: {}'.format(i, dictionary[i]))
"""
"""
up: ↑
left: ←
down: ↓
right: →
"""
"""
for (n, m) in dictionary.items():
    print(n,m)
"""
"""
up ↑
left ←
down ↓
right →
"""
# РАЗБИВАЕМ СЛОВАРЬ НА КОРТЕЖИ:
"""
print(dictionary.items())  # dict_items([('up', '↑'), ('left', '←'), ('down', '↓'), ('right', '→')])
print(*dictionary.items())  # ('up', '↑') ('left', '←') ('down', '↓') ('right', '→')
"""

# МНОЖЕСТВА:
"""
colors = set()
print(colors)  # set()

colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}

colors.add('black')  # Добавление элемента
print(colors)  # {'green', 'black', 'red', 'blue'}

colors.remove('black')  # Удаление элемента (если нет элемента - выдаёт ошибку)
print(colors)  # {'blue', 'green', 'red'}

colors.discard('black')  # Удаление элемента (если нет элемента - не выдаёт ошибку)
print(colors)  # {'blue', 'green', 'red'}

colors.clear()  # Удаление всех элементов. Остаётся пустое множество
print(colors)  # set()
"""
# ОПЕРАЦИИ СО МНОЖЕСТВАМИ:
"""
set_a = {1, 2, 3, 5, 8}
print(set_a)
set_b = {2, 5, 8, 13, 21}
print(set_b)
"""
"""
c = set_a.copy()  # Копирование   ={1, 2, 3, 5, 8}
#print(c)

u = set_a.union(set_b)  # Объединение  ={1, 2, 3, 5, 8, 13, 21}
print(u)

i = set_a.intersection(set_b)  # Пересечение  ={8, 2, 5}
print(i)

d = set_a.difference(set_b)  # Разность  ={1, 3}
print(d)

q = set_a.union(set_b).difference(set_a.intersection(set_b)) # первое множество объеденить со вторым и вычесть пересечение первого и второго
print(q)  # {1, 21, 3, 13}
"""
# Замороженное множество:
'''
a = {1, 8, 6}
b = frozenset(a)
print(type(b))
'''
# Генератор списков (list comprehension:
'''
list_1 = [7 for i in range(5)]
print(list_1)  # [7, 7, 7, 7, 7]
'''
'''
list_2 = [i for i in range(7)]
print(list_2)  # [0, 1, 2, 3, 4, 5, 6]
'''

# ПРИМЕР 1 - Список от 10 до 30:
'''
list_1 = [i for i in range(10, 31)]
print(list_1)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
'''
# ПРИМЕР 2 - Список чётных чисел от 10 до 30:
'''
list_2 = [i for i in range(10, 31) if i % 2 == 0]
print(list_2)  # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
'''
# ПРИМЕР 3 - Список пар (кортежей) чётных и нечётных чисел от 10 до 15:
'''
list_3 = [(i, i+1) for i in range(10, 16) if i % 2 == 0]
print(list_3)  # [(10, 11), (12, 13), (14, 15)]
'''
# ПРИМЕР 4 - Список целых чисел от 0 до 5, делённых на 2:
'''
list_4 = [i/2 for i in range(6)]
print(list_4)  # [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
'''
# САМЫЕ ЧАСТЫЕ ОШИБКИ:

# 1. Нет : в конце строк условий и циклов.
# 2. Нет отступов в теле условий и циклов.
# 3. Сложение (мат операции) строчных и числовых переменных:
'''
a = 'python'
b = 5
print(a + b)  # TypeError: can only concatenate str (not "int") to str
'''
# 4. Деление на ноль. ZeroDivisionError: division by zero
# 5. Ошибка ключа - изпользование не существующего ключа в словаре. KeyError:
# 6. Неправильное имя переменной NameError:
# 7. Ошибка значения - неправильное приведение типов переменных:
'''
a = 'python'
print(int(a))  # ValueError: invalid literal for int() with base 10: 'python'
'''
a = '777'
print(int(a))  # 777





