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

class ExploreSearch(object):
    def __init__(self, vib_func, dot, step_X, step_Y):
        self.vib_func = vib_func
        self.dot = dot
        self.step_X = step_X
        self.step_Y = step_Y
        
        self.dot_min = self.explore_search(self.vib_func, self.dot, self.step_X, self.step_Y)

###########################    
    def incr_X(self, koord, step_X):
        return [koord[0] + step_X, koord[1]]
    
    def decr_X(self, koord, step_X):
        return [koord[0] - step_X, koord[1]]
    
    def incr_Y(self, koord, step_Y):
        return [koord[0], koord[1] + step_Y]
    
    def decr_Y(self, koord, step_Y):
        return [koord[0], koord[1] - step_Y]
############################
            
    def compare_dots(self, vib_func, dot, dot_new):  # сравнение значний функции в двух точках
        f = func(vib_func,dot)
        f_new = func(vib_func,dot_new)
        if f_new < f:
            return True
        else:
            return False
        
    def change_coord(self, vib_func, i, dot, step_X, step_Y):  # текущее изменение координаты
        dot_new = []
        
        if i == 1:
            dot_new = self.incr_X(dot, step_X)
        elif i==2:
            dot_new = self.decr_X(dot, step_X)
        elif i==3:
            dor_new = self.incr_Y(dot, step_Y)
        elif i==4:
            dot_new = self.decr_Y(dot, step_Y)
        
        print "x_new = {0}".format(dot_new)
        print "f_new = {0}".format(func(vib_func, dot_new))
            
        compare = self.compare_dots(vib_func, dot, dot_new)
        if compare == True:
            koord = dot_new
        elif compare == False and i < 5:
            koord = self.change_coord(vib_func, i+1, dot, step_X, step_Y)
        return koord

    def explore_search(self, vib_func, dot, step_X, step_Y):  # исседующий поиск
        dot_min = self.change_coord(vib_func, 1, dot, step_X, step_Y)
        
        if dot_min == dot:
            step_X = step_X / 10
            step_Y = step_Y / 10
            dot_min = self.change_coord(vib_func, 1, dot, step_X, step_Y)
            i = i+1
            
            try:
                if i == 9:
                    raise ValueError
            except ValueError:
                 print "%s" % unicode('С текущими значениями расчет невозможен. Попробуйте еще раз!', 'utf-8')
                
        return dot_min
    
vib_func = 2
dot = {0:[0.001,0.0001]}
step_X = 0.0001
step_Y = 0.0001

test1 = ExploreSearch(vib_func, dot[0], step_X, step_Y)
print test1.dot_min

    
