# -*- coding: utf-8 -*-

import func as calculate

class ExploreSearch(object):
    
    def __init__(self, no_func, dot, step_X, step_Y):
        self.no_func = no_func
        self.step_X = step_X
        self.step_Y = step_Y
        
        self.array = {}

        self.dot_min = None 
        
        self.search(dot)
        
###########################    
    def incr_X(self, dot):
        return [dot[0] + self.step_X, dot[1]]
    
    def decr_X(self, dot):
        return [dot[0] - self.step_X, dot[1]]
    
    def incr_Y(self, dot):
        return [dot[0], dot[1] + self.step_Y]
    
    def decr_Y(self, dot):
        return [dot[0], dot[1] - self.step_Y]
############################

    def compare_dots(self, dot, dot_new):  # сравнение значний функции в двух точках
        f = calculate.func(self.no_func, dot)
        f_new = calculate.func(self.no_func, dot_new)
        if f_new < f:
            return True
        else:
            return False
        
    def change_coord(self, i, dot):  # текущее изменение координаты   
        if i == 1:
            self.array[i] = self.incr_X(dot)
        elif i==2:
            self.array[i] = self.decr_X(dot)
        elif i==3:
            self.array[i] = self.incr_Y(dot)
        elif i==4:
            self.array[i] = self.decr_Y(dot)
        
        return self.array[i]
    
    def search(self, dot):
        for i in xrange(1, 5, 1):            
            dot_new = self.change_coord(i, dot)
            comp = self.compare_dots(dot, dot_new)
            
            if comp == True:
                self.dot_min = dot_new
                break

        

#no_func = 1
#dot = {0:[1,1]}
#step_X = 10
#step_Y = 10

#test1 = ExploreSearch(no_func, dot[0], step_X, step_Y)

#print test1.array[1]
#print "dot_min = {0}".format(test1.dot_min)

#for i in test1.array:
#    print test1.array[i]