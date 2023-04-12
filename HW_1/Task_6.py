# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
# за проезд и получали билет с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. 
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# print('Введите шестизначный номер билета')
# tiket_numb = int(input())
tiket_numb = 123456
first_numb = tiket_numb // 100000 + tiket_numb // 10000 % 10 + tiket_numb // 1000 % 10
print(f"Сумма первых трех цифр: {tiket_numb // 100000} + {tiket_numb // 10000 % 10 } + {tiket_numb // 1000 % 10} = {tiket_numb // 100000 + tiket_numb // 10000 % 10 + tiket_numb // 1000 % 10}")
second_numb = tiket_numb % 1000 // 100 + tiket_numb % 100 // 10 + tiket_numb % 10
print(f"Сумма последних трех цифр: {tiket_numb % 1000 // 100} + {tiket_numb % 100 // 10 } + {tiket_numb % 10} = {tiket_numb % 1000 // 100 + tiket_numb % 100 // 10 + tiket_numb % 10}")

if first_numb == second_numb:
    print('У ВАС СЧАСТЛИВЫЙ БИЛЕТИК!!!')
else:
    print('В этот раз не повезло :(')