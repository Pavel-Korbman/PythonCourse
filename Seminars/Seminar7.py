# ПРИМЕРЫ лямбда функции
# Именная функция:
'''
def f(*args):   # На входе аргументы (позиционные аргументы)
    return sum(args)

print(f(5, 6, 7))
'''
import math

# Анонимная функция lambda:
'''
func = lambda *args: sum(args)
print(func(5, 6, 7))
print((lambda *args: sum(args))(5, 6, 7))


def func_1(**kwargs):
    return sum(kwargs.values())  # values() возвращает значения
#    return kwargs['a'] + kwargs['b'] + kwargs['c']
#    pass  # Заглушка


print(func_1(a=1, b=2, c=4))
'''
# Задача №47
'''
У вас есть код, который вы не можете менять
(так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
а нужно получить его как есть. Напишите такое лямбда-выражение transformation,
чтобы transformed_values получился копией values.
Пример ввода и вывода данных:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print(‘ok’)
else:
    print(‘fail’)
'''

# МОЁ РЕШЕНИЕ
'''
def transformation(val):
    return val

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
'''
# МОЁ РЕШЕНИЕ 2
'''
transformation = lambda val: val

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
'''
# СЕМИНАРСКОЕ РЕШЕНИЕ
'''
transformation = lambda val: val

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
'''

# Задача №49
'''
Планеты вращаются вокруг звезд по эллиптическим орбитам. 
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
Напишите функцию find_farthest_orbit(list_of_orbits), 
которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
зато искусственные спутники были были запущены на круговые орбиты. 
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
При решении задачи используйте списочные выражения. 
Подсказка: 
проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, 
а затем найти и сам эллипс, имеющий такую  площадь. 
Гарантируется, что самая далекая планета ровно одна
Пример ввода и вывода данных:
Ввод: 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
print(*find_farthest_orbit(orbits)) 
Вывод: 
2.5 10
'''

# МОЁ РЕШЕНИЕ
'''
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def find_farthest_orbit(orbits):
    orbits = [el for el in orbits if el[0] != el[1]]
    s = [math.pi * el[0] * el[1] for el in orbits]
    return orbits[s.index(max(s))]
'''

# СЕМИНАРСКОЕ РЕШЕНИЕ
'''
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    orbits = [el for el in orbits if el[0] != el[1]]
    return max(orbits, key=lambda s: math.pi * s[0] * s[1])


print(*find_farthest_orbit(orbits))
'''
# Задача №51
'''
Напишите функцию same_by(characteristic, objects), 
которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values): 
    print(‘same’) 
else: 
    print(‘different’)

Вывод: 
same

'''

# МОЁ РЕШЕНИЕ
'''
def same_by(func, lst):
    prop = list(map(func, lst))
    res = True
    for el in prop:
        if el != prop[0]:
            res = False
    return res
'''

# СЕМИНАРСКОЕ РЕШЕНИЕ
'''
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
'''

# ДОМАШКА
# Задача 1
'''
Напишите функцию print_operation_table(operation, num_rows, num_columns), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

На входе:

print_operation_table(lambda x, y: x * y, 3, 3)

На выходе:

1 2 3
2 4 6 
3 6 9
'''

'''
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            row = []
            for j in range(1, num_columns + 1):
                row.append(operation(i, j))
            print(*row)


print_operation_table(lambda x, y: x * y, 3, 3)
# print_operation_table(lambda x, y: x + y, 4, 4)
# print_operation_table(lambda x, y: x - y, 5, 5)
#print_operation_table(lambda x, y: x * y)

'''

# Задача 2
'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: 
Количество фраз должно быть больше одной!.
На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
На выходе:
Парам пам-пам
'''
stroka = 'пара-ра-рам'
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

def glasnie (lst):
    return [1 for el in lst if el.lower() in ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']]

fraza = stroka.split()
if len(fraza) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    letters = list(map(list, fraza))
    numbers = list(map(glasnie, letters))
    res = set(list(map(len, numbers)))
    if len(res) > 1:
        print('Пам парам')
    else:
        print('Парам пам-пам')



    # print(letters)
    # print(numbers)
    # print(res)
