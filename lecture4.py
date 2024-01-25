# print(5,8,6)
# a=123
# b=1.23
# print(a)
# c = None
# n=1.89
#print(n)
# n="fdg"
# print(n)
# n='fog'
'''
n="work \"yes\""
print(n)
n="fdg"
print(type(n))
'''
"""
n="work \"yes\""
print(n)
n="fdg"
print(type(n))
"""

# n=400
# a="Hello"
# b='World'
# c='Hello"World"'
# print(c)
# print(a)
# print(b)
# print(a, b, type(a))

# a=5
# b=4.9999
# c='Hello'
# print(a,'-',b,'-',c)
# print(f"{a} и {b} - {c}")
# print("{}и{} - {}".format(a,b,c))

# print('Введите значение а:')
# a=int (input())
# b=int (input('Введите второе число: '))
# print(f'{a}+{b}=',a+b)

# c=5.789
# print(type(c))
# c=int(c)
# print(type(c))

# print('Введите значение а:')
# a=float(input())
# b=int(input('Введите второе число: '))
# print(f'{a}:{b}=',a/b)

# a=5.89956
# b=6.556551
# print(a*b)
# print(round(a*b,2))

# iter=3
# print(iter)
# iter+=2
# print(iter)
# iter-=3
# print(iter)
# iter*=10
# print(iter)
# iter/=2
# print(iter)
# iter//=2
# print(iter)
# iter%=1.5
# print(iter)
# iter**=2
# print(iter)

# a=1>4
# print(a)

# a=1<4 and 5>2
# print(a)
'''
a=1==3
print(a)

a=1!=3
print(a)

a='qwe'
b='qwe'
print(a==b)

a=1<3<5<10
print(a)
'''

# userName=input('Ваше имя:')
# if userName=='Ева':
#     print(f'Ура! Это же {userName}!')
# elif userName=='Павел':
#     print(f'Это опять Вы, {userName}?')
# elif userName=='Лена' or userName=='Елена':
#     print(f'И снова здравствуйте, {userName}!')
# else:
#     print(f'Идите на фиг, {userName}!')

# n = 423 
# summa = 0 
# while n > 0: 
#     x = n % 10 
#     summa = summa + x 
#     n = n // 10 
# print(summa) # 9

# i = 0 
# while i < 5:    
#     #if i == 3:        
#         #break    
#     i = i + 1 
# else:    
#     print('Пожалуй')    
#     print('хватит )') 
# print(i)

# # Пользователь вводит число, необходимо найти минимальный делитель данного числа 
# # Решение: 
# n = int(input()) 
# flag = True 
# i = 2 
# while flag:    
#     if n % i == 0: # если остаток при делении числа n на i равен 0        
#         flag = False        
#         print(i)    
#     elif i > n // 2: # делительь числа не может превышать введенное число, деленное на 2       
#         print(n)       
#         flag = False    
#     i += 1

# for i in 1, -2, 3, 14, 5:     
#     print(i)

# r = range(5) # 0 1 2 3 4 диапазон до 5 шаг 1
# r = range(2, 5) # 2 3 4 диапазон от 2 до 5 шаг 1
# r = range(-5, 0) # -5 -4 -3 -2 -1
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# for i in r: 
# for i in range(100, 0, -20): 
#     print(i)

# a='qwerty'
# print(a[2])
# print()
# for i in a: 
#     print(i)
# print()
# for i in 'qwerty': 
#     print(i)

# line = "" 
# for i in range(5):    
#     line = ""    
#     for j in range(5):        
#         line += "*"    
#     print(line)

#text = 'СъЕШЬ ещё этих МяГкИх французских булок' 

# print(len(text)) # 39 - количество символов
# print('ещё' in text) # True есть ли это в тексте
# print(text.lower()) # съешь ещё этих мягких французских булок 
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК 
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

text = 'ABCD1N' 
# print(text[0])  # A
# print(text[1])  # B
# print(text[len(text)-1])  # N
# print(text[-3])  # D 
# print(text[:])  # ABCD1N
# print(text[:2]) # AB
# print(text[len(text)-3:]) # D1N
# print(text[2:4]) # CD
# print(text[0:-1]) # ABCD1
# print(text[0:len(text):2]) # AC1
print(text[::3]) #A D
print(text[2:4] + text[-3] + text[:2])  # CDDAB