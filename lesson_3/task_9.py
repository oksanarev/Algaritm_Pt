# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
M = 10
N = 5
a = []
for i in range(N):
    b = [random.randint(0, 49) for _ in range(M)]
    print(b)
    a.append(b)
    print()
mx = -1
for j in range(M):
    mn = 49
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
