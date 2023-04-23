# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X . 
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

quant_numbers = abs(int(input('Введите количество чисел: ')))
number = [randint(1, 10) for i in range(quant_numbers)]
print(number)
x = int(input('Задайте число для сравнения: '))
min_differ = number[0]
for i in number:
    differ = abs(i - x)
    if differ < min_differ:
        result = i
        min_differ = differ
        
# result = min([i for i in number if abs(i - x) == min_differ])
print(f'Самый близкий элемент к заданному числу: {result} ')