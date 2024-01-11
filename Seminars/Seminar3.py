"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
#list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
#print(len(set(list_1)))
"""
list_2 = []
for el in list_1:
    if el not in list_2:
        list_2.append(el)
print(len(list_2))
"""
'''
list_3 = []
for i in range(len(list_1)):
    if list_1[i] not in list_3:
        list_3.append(list_1[i])
print(len(list_3))
'''

"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""
'''
list_1 = [1, 2, 3, 4, 5]
k = 3
'''
"""
new_lst = list_1[k:] + list_1[:k]
print(*new_lst)
"""
"""
for i in range(k-1):
    last_el = list_1.pop()
    list_1.insert(0,last_el)
print(*list_1)
"""
"""
Задача №21.
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

#lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
 #          {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
'''
#ТРАДИЦИОННЫЙ ИТЕРАТОР
new_set = set()

for el in lst_obj:
    for val in el.values():
        new_set.add(val)
print(new_set)
'''
#ВКЛЮЧЕНИЕ
#print(set(val for el in lst_obj for val in el.values()))
'''

Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""

lst_1 = [0, -1, 5, 2, 3]
count = 0
for i in range(1,len(lst_1)):
    if lst_1[i] > lst_1[i-1]:
        count+= 1
print(count)
# Вывести чётные
res_01 = []
for el in lst_1:
    if el % 2 == 1:
        res_01.append(el)
print(res_01)

# Вывести не чётные элементы с чётн индексами
res_02 = []
for i in range(0, len(lst_1),2):
    if lst_1[i] % 2 == 1:
        res_02.append(lst_1[i])
print(res_02)
'''
# ДОМАШКА

#1 ЗАДАЧА:
'''
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 3
# 1
'''
'''
list_1 = [1, 2, 3, 4, 5]
k = 3
count = 0
for element in list_1:
    if element == k:
        count += 1
print(count)

# ЭТАЛОН:
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)
'''

#2 ЗАДАЧА:
'''
Требуется найти в массиве list_1 
самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. 
Если значение k совпадает с этим элементом - выведите его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
'''
'''
list_1 = [1, 2, 3, 4, 5]
k = 6
delta = min([abs(val - k) for val in list_1])
if (k - delta) in list_1:
    print(k - delta)
else:
    print(k + delta)

# ЭТАЛОН
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
'''

#3 ЗАДАЧА:
'''
Скрабл


В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
Пример:
k = 'ноутбук'
# 12
'''

k = 'ноутбук'
'''
word = k.upper()
str_1 = 'AEIOULNSTRАВЕИНОРСТ'
str_2 = 'DGДКЛМПУ'
str_3 = 'BCMPБГЁЬЯ'
str_4 = 'FHVWYЙЫ'
str_5 = 'KЖЗХЦЧ'
str_8 = 'JXШЭЮ'
str_10 = 'QZФЩЪ'
value = 0
for letter in word:
    if letter in str_1:
        value += 1
    elif letter in str_2:
        value += 2
    elif letter in str_3:
        value += 3
    elif letter in str_4:
        value += 4
    elif letter in str_5:
        value += 5
    elif letter in str_8:
        value += 8
    elif letter in str_10:
        value += 10
print(value)
'''
# ЭТАЛОН
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)
