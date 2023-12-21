"""
Задача №1. Решение в группах
Семинар 1. Ввод-вывод, операторы ветвления
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.

Input:
n = 700
m = 750
Output:
2

from math import ceil
n=700
m=750
# print(ceil(m/n))
print((m+n-1)/)
"""
"""
Задача №3. Решение в группах
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32

a, b, c = 20, 21, 22
print(a//2 + a%2 +b//2+b%2 +c//2+c%2)
"""
"""
Задача №5. Решение в группах
Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6

i, j = 3, 4
if i!=j:
    print((i+j)-1)
else:
    print('Задача не решается')
"""
"""
Задача №7. Решение в группах
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES
"""
"""
year = 2016
if year % 4 ==0 and year % 100 != 0 or year % 400 ==0:
    print('Високостный')
else:
    print('Не')
    """
# year = 2016
# print('Yes' if year % 4 ==0 and year % 100 != 0 or year % 400 ==0 else 'No')


"""
ДОМАШКА

1. ЗАДАЧА:
Найдите сумму цифр трехзначного числа n
"""
# n = int(input())
# res = n//100 + n%100//10 + n%10
# print(res)

"""
2. ЗАДАЧА:
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
"""
#n = int(input())
#petya = n//6
#serega = petya
#katya = 4*petya
#print(f'{petya} {katya} {serega}')

"""
3. ЗАДАЧА:
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, 
которая проверяет счастливость билета с номером n и выводит на экран yes или no
"""
#n = int(input())

##left_sum = n//100000 + n%100000//10000 + n%10000//1000
##right_sum = n%1000//100 + n%100//10 + n%10

#print('yes' if n//100000 + n % 100000//10000 + n % 10000//1000 == n % 1000//100 + n % 100//10 + n%10 else 'no')

"""
4. ЗАДАЧА:
Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
Выведите yes или no соответственно.
"""
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
print('yes' if c >= a and c % a == 0 or c >= b and c % b == 0 else 'no')