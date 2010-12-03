# -*- coding: utf-8 -*-

import func as calculate
import explore_search as explore
import input as value

def handler_ExploreSearch(no_func, eps, x0, step_X, step_Y):
    while True:
        exp = explore.ExploreSearch(no_func, x0, step_X, step_Y)
        print exp.array.values()
        
        if exp.dot_min == None:  # исследующий поиск неудачен
            
            if abs(step_X) <= eps and abs(step_Y) <= eps:
                result = 'SEARCH_FAILED'
                break  
                          
            elif abs(step_X) > eps and abs(step_Y) > eps:
                step_X = step_X / alpha
                step_Y = step_Y / alpha
                
            elif abs(step_X) > eps and abs(step_Y) <= eps:
                step_X = step_X / alpha
            
            elif abs(step_X) <= eps and abs(step_Y) > eps:
                step_Y = step_Y / alpha
                
        else:
            result = 'SEARCH_SUCSESS'
            break
    
    if result == 'SEARCH_SUCSESS':
        return [result, exp.dot_min]
    elif result == 'SEARCH_FAILED':
        return [result, exp.array[4]]

if __name__ == '__main__':
    text = "%s" % unicode('Выберите функцию: ', 'utf-8')
    vib_func = value.input(text, type="int", min=1, max=3)
    
    text = "%s" % unicode('Введите точность вычислений: ', 'utf-8')
    eps = value.input(text, type="float")
    
    text = "%s" % unicode('Введите координату x1 начальной точки: ', 'utf-8')
    x0_X = value.input(text, type="float")
    text = "%s" % unicode('Введите координату x2 начальной точки: ', 'utf-8')
    x0_Y = value.input(text, type="float")
    
    text = "%s" % unicode('Введите шаг по координате X: ', 'utf-8')
    step_X = value.input(text, type="float")
    text = "%s" % unicode('Введите шаг по координате Y: ', 'utf-8')
    step_Y = value.input(text, type="float")
    
    x = {}
    x = {0:[x0_X,x0_Y]}
    alpha = 10  # коэффициент затуния
    
    print "x = {0}".format(x[0])
    print "f = {0}".format(calculate.func(vib_func,x[0]))
    explore_result = handler_ExploreSearch(vib_func, eps, x[0], step_X, step_Y)
    print "explore_result = {0}".format(explore_result) 
    