# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите 1-е число: '))
b = int(input('Введите 2-е число: '))
c = int(input('Введите 3-е число: '))

if b < a < c or c < a < b:
    print(f'Среднее число: {a}')
elif a < c < b or b < c < a:
    print(f'Среднее число: {c}')
else:
    print(f'Среднее число: {b} ')

