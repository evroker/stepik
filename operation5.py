# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.
#
# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.
num = int(input())
num2 = int(input())
num3 = int(input())
if (num2 - num) + num2 == num3:
    print('YES')
else:
    print('NO')
