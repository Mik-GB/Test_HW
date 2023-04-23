# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.

first_number = int(input('Введите количество элементов первого множества: '))
second_number = int(input('Введите количество элементов второго множества: '))

list_1 = []
list_2 = []
for i in range(first_number):
    first = 'Введите ' + str(i + 1) + ' число первого множества: '
    list_1.append(input(first))
for i in range(second_number):
    second = 'Введите ' + str(i + 1) + ' число второго множества: '
    list_2.append(input(second))
print(list_1)
print(list_2)
# result_1 = set(list_1)
# result_2 = set(list_2)
# result = sorted(result_1.intersection(result_2))
result = sorted(set(list_1).intersection(set(list_2)))
print(*result)
