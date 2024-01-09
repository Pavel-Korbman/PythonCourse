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
"""
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







