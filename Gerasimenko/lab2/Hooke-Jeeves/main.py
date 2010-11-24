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

def input_data(text):
    print text
    
    try:
        data = float(raw_input())
    except (TypeError, ValueError):
        print "%s" % unicode('Введены недопустимые символы. Попробуйте еще раз!', 'utf-8')
        data = input_data(text)
        
    return data

if __name__ == '__main__':
    text = "%s" % unicode('Введите координату x1 начальной точки: ', 'utf-8')
    x0_X = input_data(text)
    text = "%s" % unicode('Введите координату x2 начальной точки: ', 'utf-8')
    x0_Y = input_data(text)
    
    text = "%s" % unicode('Введите шаг по координате X: ', 'utf-8')
    step_X = input_data(text)
    text = "%s" % unicode('Введите шаг по координате Y: ', 'utf-8')
    step_Y = input_data(text)
    
    x = {}
    x = {0:[x0_X,x0_Y]}
    
    print "x = {0}    y = {1}".format(x0_X, x0_Y)
    
    f = func(1,x[0])
    print f
