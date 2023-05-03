# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 
def summ(numb_a, numb_b):
    numb_a = abs(numb_a)
    numb_b = abs(numb_b)
    if numb_a == 0:
        return numb_b
    if numb_b == 0:
        return numb_a
    else:
        return summ(numb_a + 1, numb_b - 1)
print(summ(-9, -9))   