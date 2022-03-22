# 1. Выполнить логические побитовые операции "И", "ИЛИ" и др. над
# числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и
# влево на два знака.

a = 5
print(f'5 в битах: {a} = {bin(a)}')
b = 6
print(f'6 в битах: {b} = {bin(b)}')

print(f'Побитовая опперация "И": 5 & 6 = { a & b}, {bin(a & b)}')

print(f'Побитовая опперация "ИЛИ": 5 | 6 = {5|6}, {bin(5|6)}')

print(f'Побитовая опперация "Исключения ИЛИ": 5 ^ 6 = {5^6}, {bin(5^6)}')

print(f'Сдвиг влево 5 << 2  = {5<<2}, {bin(5<<2)}')

print(f'Сдвиг вправо 5 >> 2  = {5>>2}, {bin(5>>2)}')
