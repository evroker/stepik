# Напишите программу, которая определяет наименьшее из четырёх чисел.
#
# Формат входных данных
# На вход программе подаётся четыре целых числа.
#
# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b and b < c and c < d:
    print (a)
else:
    if b < c < d:
        print (b)
    else:
        if c < d:
            print (c)
        else:
            print (d)