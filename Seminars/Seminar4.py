# ЗАДАЧИ МОИ РЕШЕНИЯ

# Задача №25
'''
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
'''
'''
string = 'a a a b c a a d c d d'
list_1 = string.split()
count = 0
for i in range(len(list_1)):
    for j in range(len(list_1)):
        if list_1[j] == list_1[i]:
            count +=1
            if count > 1:
                list_1[j] =list_1[j] + '_' + str(count-1)
    count = 0
print(*list_1)
'''

# Задача №27
'''
Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте. 
Input: 
She sells sea shells on the sea shore 
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore 
I'm sure that the shells are sea shore shells 
Output: 
13
'''
'''
string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
letters = string.upper().split()
dif_letters = set(letters)
#print(letters)
print(len(dif_letters))
'''

# ЗАДАЧИ РЕШЕНИЯ НА СЕМИНАРЕ

# Задача №25
'''
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
'''
'''
lst = input('Введите символы через пробел:').split()
my_dict = {}
for el in lst:
    if el not in my_dict:
        print(el, end=' ')
    else:
        print(f'{el}_{my_dict[el]}', end=' ')
    my_dict[el] = my_dict.get(el, 0) + 1
'''
# Задача №27
'''
Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте. 
Input: 
She sells sea shells on the sea shore 
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore 
I'm sure that the shells are sea shore shells 
Output: 
13
'''
'''
string = """She sells sea shells on the sea shore 
The shells that she sells are sea shells 
I'm sure.So if she sells sea shells on the sea shore 
I'm sure that the shells are sea shore shells""".upper().split()
# print(len(set(string.upper().split())))
print(len(set(string)))
'''

# ctrl + alt + l  Нажать для исправления стиля
# ctrl + / Закоментировать выделенное

# Задача №27
'''
Задача №29. 
Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
“Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, 
которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
Однако 2  друга оказались не такими смышлеными. 
Никто из ребят не смог до конца сделать это задание. 
Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
За помощью товарищи обратились к Вам, студентам.

Ваня: 
n = int(input()) 
max_number = 1000 
while n != 0:   
    n = int(input())   
    if max_number > n:       
        max_number = n 
print(max_number)

Петя: 
n = int(input()) 
max_number = -1 
while n < 0:   
    n = int(input())   
    if max_number < n:       
        n = max_number 
print(n)
'''
'''
n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
'''
# ФУНКЦИИ:
'''
Есть 2 группы пользовательских функций: Именные и Анонимные
'''
# ИМЕННЫЕ функции:
'''
def func(): # def - имя функции. Функция вызывается именем
    res = 2 + 2
    return res
a = func()
print(a)
print (func())
'''
'''
def quad(a, b):
    res = a + b
    return res

c = quad(3, 5)  # Позиционные переменные - принимают значения по позиции
d = quad(5, 3)
'''

'''
def quad(a, b):
    res = a + b
    return res


c = quad(a=3, b=5)  # Пприсваемые переменные - принимают значения по именам переменных (именованные переменные)
print(c)
'''
'''
def summ(a, b=0):  # a - обязательный элемент
    res = a + b
    return res


c = summ(a=3)
print(c)
'''
'''
# АНОНИМНЫЕ функции (для простых математических выражений:

extent = lambda x, y: x ** y

print(extent(2, 4))

# ФУНКЦИЯ ОТ КОРТЕЖА ЭЛЕМЕНТОВ (сколько угодно элементов)

def function(*args):  #  *args - кортеж
    return args[0] + args[1] + args[2]

print(function(1, 2, 8))


# ФУНКЦИЯ ОТ СЛОВАРЯ
def function_1(**kwargs):  #  **kwargs - словарь
    return kwargs['a'] + kwargs['b'] + kwargs['c']

print(function_1(a=1, b=2, c=11))
'''

# ДОМАШКА

# Задача 1
'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:


var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
'''
'''
var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '5 2 3 4 '

# l_2, l_3 = int(var1.split()[0]), int(var1.split()[1])
print(*sorted(set([int(i) for i in var2.split()]).intersection([int(j) for j in var3.split()])))
'''

# Задача 2
'''
В фермерском хозяйстве в Карелии выращивают чернику. 
Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. 
Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.

Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.
В фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. 
Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

Ваша задача - написать программу, которая определит максимальное число ягод, 
которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

Входные данные:
На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. 
Размер списка не превышает 1000 элементов.

Выходные данные:
Программа должна вывести одно целое число - максимальное количество ягод, 
которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.

Пример использования 
На входе:
arr = [5, 8, 6, 4, 9, 2, 7, 3]
На выходе:
19
'''
'''
arr = [5, 8, 6, 4, 9, 2, 7, 3]
arr.append(arr[0])
arr.append(arr[1])
print(max([arr[i] + arr[i + 1] + arr[i + 2] for i in range(len(arr) - 2)]))
# berries = [arr[i] + arr[i + 1] + arr[i + 2] for i in range(len(arr) - 2)]
# print(max(berries))
# print(arr)
'''