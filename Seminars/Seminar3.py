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

lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
'''
#ТРАДИЦИОННЫЙ ИТЕРАТОР
new_set = set()

for el in lst_obj:
    for val in el.values():
        new_set.add(val)
print(new_set)
'''
#ВКЛЮЧЕНИЕ
print(set(val for el in lst_obj for val in el.values()))
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

