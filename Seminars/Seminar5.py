# Задача №25
'''
Последовательностью Фибоначчи называется последовательность чисел
a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''

# Решение циклом:
'''
n = int(input('Введите номер числа Фибоначчи:'))
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)

for i in range(2, n + 1):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
print(fibonacci[n])
'''
'''
n = 7
fibo_p, fibo_n = 0, 1
for _ in range(n):
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
print(fibo_n)
'''

# Решение рекурсией:
'''
def fibo(n, fibo_p=0, fibo_n=1):
    i = 0
    if n ==0:
        return fibo_n
    return fibo(n - 1, fibo_n, fibo_p + fibo_n)

print(fibo(7))
'''

# Задача №33:
'''
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
Input: 5 -> 1 3 3 3 4 
Output: 1 3 3 3 1
'''

# Решение циклом:

# Моё решение:
'''
score = [1, 3, 3, 3, 4]
score_max = max(score)
score_min = min(score)
for i in range(len(score)):
    if score[i] == score_max:
        score[i] = score_min
print(score)
'''

# Семинарское решение:
'''
lst = [1, 3, 3, 3, 4]
max_n, min_n = max(lst), min(lst)
lst_1 = []
for el in lst:
    if el == max_n:
       lst_1.append(min_n)
    else:
        lst_1.append(el)
print(lst_1)
'''

# Решение рекурсией:
'''
lst = [1, 3, 3, 3, 4]
def func (lst, lst_1 =[], max_n=max(lst), min_n =min(lst)):
    if len(lst) == 0:
        return lst_1
    if lst[0] == max_n:
        lst_1.append(min_n)
    else:
        lst_1.append(lst[0])
    return func(lst[1:])  # Возвращаем массив без первого элемента и так пока длинна не дойдёт до 0

print(func(lst))
'''

# Задача №35:
'''
Напишите функцию, которая принимает одно число и проверяет, 
является ли оно простым. 
Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
Input: 5 
Output: yes
'''

# Решение циклом:
'''
def func_1(n):
    if n == 1 or n == 2 or n == 0:
        return True
    for divider in range(3, n):
        if n % divider == 0:
            return False
        return True


print(func_1(1))
'''

# Решение рекурсией:
'''
def func_1(n, divider=2):
    if n == 1 or n == 2 or n == 0:
        return True
    if divider < n:
        if n % divider == 0:
            return False
        return func_1(n, divider+1)
    return True
print(func_1(13))
'''

# Задача №37:
'''
Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке. 
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). 
Input:    2 -> 3 4 
Output: 4 3
'''
# Решение циклом:
'''
my_str = '3 4 8 9'


def func_1(a):
    res = ''
    for el in reversed(a):
        res += el
    return res


print(func_1(my_str))
'''

# Решение рекурсией:
'''
my_str = '3 4 8 9'

def func_2(b):
    if len(b) == 1:
        return b
    return b[-1] + func_2(b[:-1])  # func_2(b[:-1]) Укорачиваем строку на 1 элемент в каждой рекурсии


print(func_2(my_str))
'''

# Задача дополнительная:

'''
Обойти и суммировать элементы от 0 до n без цикла:
'''

# Моё решение:
'''
def func_1(n):
    if n == 1:
        return n
    res = n + func_1(n - 1)
    return res


print(func_1(3))
'''

# Семинарское решение:
'''
def func_2(n, summ=0, num=0):
    if num == n+1:
        return summ
    return func_2(n, summ+num, num+1)


print(func_2(3))
'''
# ДОМАШКА:

# Задача 1:
'''
Напишите функцию f, которая на вход принимает два числа a и b, 
и возводит число a в целую степень b с помощью рекурсии.
Функция не должна ничего выводить, только возвращать значение.

Пример:

a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8 
'''
'''
def f(a, b):
    if b == 1:
        return a
    res = a * f(a,b - 1)
    return res

a = 3
b = 5
print(f(a, b))
'''

# Задача 2:
'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
Функция не должна ничего выводить, только возвращать значение.

Пример:
sum(2, 2)
# 4
'''


def summ(a, b):
    if b == 0:
        return a
    res = summ(a+1, b - 1)
    return res


a = 10
b = 23
print(summ(a, b))
