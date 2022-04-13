import cProfile

#def test_ellem(func):
 #   lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875]
  #  for i, item in enumerate(lst):
   #     assert item == func(i)
    #    print(f'Test{i} OK')

def elem_list(n):
    elem_l = [None]*1000
    elem_l[:1] = [1]

    def _elem_list(n):
        s = 1
        if elem_l[n] is None:
            s += _elem_list(n - 1) / -2
            elem_l[n] = s
            #print(elem_l)
        return elem_l[n]

    return _elem_list(n)

#test_ellem(elem_list)
#print(elem_list(5))
#cProfile.run('elem_list(10)')
# 15 function calls (5 primitive calls) in 0.000 seconds
#11/1    0.000    0.000    0.000    0.000 Task_4.py:13(_elem_list)

#cProfile.run('elem_list(100)')
#105 function calls (5 primitive calls) in 0.001 seconds
#101/1    0.000    0.000    0.000    0.000 Task_4.py:13(_elem_list)

#cProfile.run('elem_list(950)')
#955 function calls (5 primitive calls) in 0.005 seconds
#951/1    0.005    0.000    0.005    0.005 Task_4.py:13(_elem_list)

# "Task_4.elem_list(10)"
#1000 loops, best of 5: 17.1 usec per loop

# "Task_4.elem_list(200)"
# 1000 loops, best of 5: 117 usec per loop

#"Task_4.elem_list(800)"
#1000 loops, best of 5: 503 usec per loop

