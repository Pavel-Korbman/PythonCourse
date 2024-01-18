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
'''
import modul_1  # Имполтируем модуль (только имя файла)
print (modul_1.max_1(2, 4))  # Вызываем функцию с указанием имени файла модуля
'''
'''
from modul_1 import max_1  # Имполтируем конкретную функцию из модуля
print(max_1(10, 40))  # Вызываем функцию без указания имени файла модуля
'''
'''
from modul_1 import *  # Имполтируем все функции из модуля
print(max_1(60, 40))  # Вызываем функцию без указания имени файла модуля
'''
'''
# Можно присвоить новое имя модулю в программе основного файла:
import modul_1 as m1
print(m1.max_1(100, 40)) # При вызове указываем новое имя
'''

# РЕКУРСИЯ:

# Задача 1:
'''
Дано число n.
Вывести n первых чисел ряда Фибоначчи.
'''
'''
def fib(m):
    if m in [1, 2]:  # Условия выхода (базис рекурсии)
        return 1
    return fib(m - 1) + fib(m - 2)

n = int(input('Введите n:'))
list_1 = []
for i in range(1, n):
    list_1.append(fib(i))
print(*list_1)
'''

# СОРТИРОВКА - БЫСТРАЯ И СЛИЯНИЕМ:

# БЫСТРАЯ СОРТИРОВКА:
'''
Дан список чисел. Нужно отсортировать по возрастанию.
Задаём число из списка - первое.
Создаём 2 списка. В один кладём все значения меньше заданного числа, в другой все значения больше заданного числа.
Складываем список с меньшими (применив рекурсию - вызвав этот метод к этому списку), 
число 
и список с большими (применив рекурсию - вызвав этот метод к этому списку).
И так пока каждый список не уменьшится до 1 элемента.
'''
'''
def quick_sort(array):
    if len(array) < 1:  # Базис рекурсии
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14,5,9,6,3,58,7,5,2,7]))  # [2, 3, 5, 5, 6, 7, 7, 9, 14, 58]
'''

# СОРТИРОВКА СЛИЯНИЕМ:

'''
Делим список пополам и получившиеся списки делим пополам полка не получаются числа. 
Соседние числа объединяем в пары, поставив сначала меньшее, затем большее.
Далее сливаем пары, упорядочивая в итоговых списках элементы по возрастанию.
'''


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):  # Цикл завершится если закончились элементы в одном из списков
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):  # На случай если остались элементы в левом списке -добавляем их
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):  # На случай если остались элементы в правом списке -добавляем их
            nums[k] = right[j]
            j += 1
            k += 1


list = [3, 1, 8, 9, 2]
merge_sort(list)
print(list)  # [1, 2, 3, 8, 9]
