# 2.По введенным пользователем координатам двух точек вывести
# уравнение прямой, которая проходит через эти точки.

print('Введите координаты точки A :')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
print('Введите координаты точки B :')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

if x1 == x2:
    k = 1
else:
    k = (y1 - y2)/(x1 - x2)
b = y2 - k * x2
print(f'Уравнение прямой, проходящей через точки A и B : y = {k}* x + {b}')

