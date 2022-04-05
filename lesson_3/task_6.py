# 6.  В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

r = [random.randint(-10, 20) for _ in range(25)]
print(f'Массив : {r}')

max = r[0]
min = r[0]
sum = 0

for i in r:
    if i > max:
        max = i
    elif i < min:
        min = i
print('Минимальное число:', min, 'максимальное число:', max)
min_ind = r.index(min)
max_ind = r.index(max)
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

for i in range(min_ind+1, max_ind):
    sum += r[i]
    print(f"{r[i]} + ", end="")
print('=', sum)
