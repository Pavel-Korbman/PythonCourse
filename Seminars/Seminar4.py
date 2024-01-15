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
string = """She sells sea shells on the sea shore 
The shells that she sells are sea shells 
I'm sure.So if she sells sea shells on the sea shore 
I'm sure that the shells are sea shore shells"""
print(len(set(string.upper().split())))