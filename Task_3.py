import cProfile

#def test_ellem(func):
 #   lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875]
  #  for i, item in enumerate(lst):
   #     assert item == func(i)
    #    print(f'Test{i} OK')

def elem_dict(n):
    elem_d = {}

    def _elem_dict(n):
        s = 1
        if n == 0:
            elem_d[n] = s
            return elem_d[n]
        s += _elem_dict(n-1) / -2
        elem_d[n] = s
#        print(elem_d)
        return elem_d[n]

    return _elem_dict(n)

#test_ellem(elem_dict)
#print(elem_dict(5))

#cProfile.run('elem_dict(10)')
# 15 function calls (5 primitive calls) in 0.000 seconds
#11/1    0.000    0.000    0.000    0.000 Task_3.py:13(_elem_dict)

#cProfile.run('elem_dict(100)')
#105 function calls (5 primitive calls) in 0.000 seconds
#101/1    0.000    0.000    0.000    0.000 Task_3.py:13(_elem_dict)

#cProfile.run('elem_dict(950)')
#955 function calls (5 primitive calls) in 0.006 seconds
#951/1    0.006    0.000    0.006    0.006 Task_3.py:13(_elem_dict)

#"Task_3.elem_dict(10)"
# 1000 loops, best of 5: 8.33 usec per loop

# "Task_3.elem_dict(200)"
# 1000 loops, best of 5: 126 usec per loop

#"Task_3.elem_dict(800)"
# 1000 loops, best of 5: 581 usec per loop
