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