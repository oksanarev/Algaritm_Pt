# 7.  В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.


import random

r = [random.randint(0, 49) for _ in range(50)]
print(f'Массив: {r}')

min_ind_1 = 0
min_ind_2 = 1

for i in r:
    if r[min_ind_1] > i:
        min_ind_2 = min_ind_1
        min_ind_1 = r.index(i)
    elif r[min_ind_2] > i:
        min_ind_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_ind_1]} и {r[min_ind_2]}')
