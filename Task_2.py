# 1. Задание 4 от 2 занятия: Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import cProfile
import functools

def test_ellem(func):
    lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test{i} OK')

@functools.lru_cache()
def ellem(n):
    s = 1
    if n > 0:
        s += ellem(n-1) / -2

    return s

#test_ellem(ellem)

#print(ellem(5))

#cProfile.run('ellem(10)')
#14 function calls (4 primitive calls) in 0.000 seconds
#11/1    0.000    0.000    0.000    0.000 Task_2.py:6(ellem)

#cProfile.run('ellem(20)')
#24 function calls (4 primitive calls) in 0.000 seconds
# 21/1    0.000    0.000    0.000    0.000 Task_2.py:6(ellem)

#cProfile.run('ellem(700)')
#704 function calls (4 primitive calls) in 0.003 seconds
# 701/1    0.002    0.000    0.002    0.002 Task_2.py:6(ellem)

# "Task_2.ellem(200)"
# 1000 loops, best of 5: 67 usec per loop

#"Task_2.ellem(200)"
#1000 loops, best of 5: 136 nsec per loop - тест с использованием декоратора


# "Task_2.ellem(800)"
# 1000 loops, best of 5: 322 usec per loop

# "Task_2.ellem(9)"
# 1000 loops, best of 5: 2.84 usec per loop

# При анализе с декоратером при помощи cProfile данные остались такими же.