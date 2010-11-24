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
###########################    
def incr_X(koord, step_X):
    koord = [koord[0] + step_X, koord[1]]
    return koord

def decr_X(koord, step_X):
    return [koord[0] - step_X, koord[1]]

def incr_Y(koord, step_Y):
    return [koord[0], koord[1] + step_Y]

def decr_Y(koord, step_Y):
    return [koord[0], koord[1] - step_Y]
############################
def compare_dots(vib_func, x, x_new):  # сравнение значний функции в двух точках
    f = func(vib_func,x)
    f_new = func(vib_func,x_new)
    if f_new < f:
        return True
    else:
        return False

def change_coord(vib_func, i, x, stepX, stepY):  # текущее изменение координаты
    x_new = []
    
    if i == 1:
        x_new = incr_X(x, stepX)
    elif i==2:
        x_new = decr_X(x, stepX)
    elif i==3:
        x_new = incr_Y(x, stepY)
    elif i==4:
        x_new = decr_Y(x, stepY)
    
    print "x_new = {0}".format(x_new)
    print "f_new = {0}".format(func(vib_func, x_new))
        
    compare = compare_dots(vib_func, x, x_new)
    if compare == True:
        koord = x_new
    elif compare == False and i<5:
        koord = change_coord(vib_func, i+1, x, stepX, stepY)
    return koord
    
def explore_search(vib_func, x, stepX, stepY):  # исседующий поиск
    x_min = change_coord(vib_func, 1, x, stepX, stepY)
    return x_min
############################ 
def input_data(text):
    print text
    
    try:
        if text == 'Выберите функцию: ':
            data = int(raw_input())
            if data < 1 or data > 3:
                raise ValueError
        else:
            data = float(raw_input())
    except (TypeError, ValueError):
        print "%s" % unicode('Введены неверные значения. Попробуйте еще раз!', 'utf-8')
        data = input_data(text)
        
    return data

if __name__ == '__main__':
    text = "%s" % unicode('Выберите функцию: ', 'utf-8')
    vib_func = input_data(text)
    
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
    
    print "x = {0}".format(x[0])
    print "f = {0}".format(func(vib_func,x[0]))
    x_min = explore_search(vib_func, x[0], step_X, step_Y)
#    print x_min
    
#    f_new2 = 0
#    f_new3 = 0
#    f_new4 = 0
    
#    i = 0
#    x_min = x[0]
#    f = func(vib_func, x[0])
    
#    i = i + 1
#    x[1] = incr_X(x[0], step_X)
#    f_new = func(vib_func, x[1])
    
#    if f_new < f:
#        x_min = x[1]
#    else:
#        x[2] = decr_X(x[0], step_X)
#        f_new2 = func(vib_func, x[2])
#        
#        if f_new2 < f:
#            x_min = x[2]
#        else:
#            x[3] = incr_Y(x[0], step_Y)
#            f_new3 = func(vib_func, x[3])
#            
#            if f_new3 < f:
#                x_min = x[3]
#            else:
#                x[4] = decr_Y[x[0], step_Y]
#                f_new4 = func(vib_func, x[4])
#                
#                if f_new4 < f:
#                    x_min = x[4]
#                else:
#                    x_min = x[0]
#        
#    
#    print "f = {0}\nf_new = {1}".format(f, f_new)
#    
#    if f_new2:
#        print "f_new2 = {0}\n".format(f_new2)
#    if f_new3:
#        print "f_new3 = {0}\n".format(f_new3)
#    if f_new4:
#        print "f_new4 = {0}\n".format(f_new4)
#    
#    for i in x:
#        print x[i]
    
    
    