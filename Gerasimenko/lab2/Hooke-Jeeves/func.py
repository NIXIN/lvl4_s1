# -*- coding: utf-8 -*-

def func(vib_func, koord):
    x1 = koord[0]
    x2 = koord[1]
    
    if vib_func == 1:
        return 12 * x1**2 + 6*x1*x2 + 2 * x2**2 - 2*x1 - x2
    elif vib_func == 2:
        return 0.5 * (x2 - x1**2)**2 + (1 - x1)**2
    elif vib_func == 3:
        return 100 * (x2 - x1**2)**2 + (1 - x1)**2