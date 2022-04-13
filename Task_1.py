# Берём 4 задание от 2занятия: найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#  Количество элементов (n) вводится с клавиатуры.



#n = int(input('Введите количество элементов: '))
e = 1
s = 0
for i in range(7):
    s += e
    e /= -2
print(s)
# C:\Users\Аэро\PycharmProjects\Alg_python\lesson_4>python -m timeit -n 1000 -s "import Task_1"
# 1000 loops, best of 5: 19.2 nsec per loop