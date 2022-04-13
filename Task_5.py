import cProfile

#def test_ellem(func):
 #   lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875]
  #  for i, item in enumerate(lst):
   #     assert item == func(i)
    #    print(f'Test{i} OK')

def sum_loop(n):
    first, second = 0, 1

    for i in range(n+1):
        first, second = second + first, second / -2
 #       print(s)
    return first

#test_ellem(sum_loop)
#print(sum_loop(5))

#cProfile.run('sum_loop(10)')
#4 function calls in 0.000 seconds
#1    0.000    0.000    0.000    0.000 Task_5.py:9(sum_loop)

#cProfile.run('sum_loop(100)')
#4 function calls in 0.000 seconds
#1    0.000    0.000    0.000    0.000 Task_5.py:9(sum_loop)

#cProfile.run('sum_loop(10000)')
# 4 function calls in 0.002 seconds
#1    0.002    0.002    0.002    0.002 Task_5.py:9(sum_loop)

# "Task_5.sum_loop(100)"
#1000 loops, best of 5: 14.2 usec per loop

#"Task_5.sum_loop(1000)"
#1000 loops, best of 5: 151 usec per loop

# "Task_5.sum_loop(5000)"
#1000 loops, best of 5: 835 usec per loop

#Самое оптимальное время выполнения кода - при использовании цикла, т.е в 5 варианте.

