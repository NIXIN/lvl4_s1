# -*- coding: utf-8 -*-

import func as calculate
import explore_search as explore
import input as value

def handler(no_func, x, alpha, step_X, step_Y):
    while True:
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
            
        exp = explore.ExploreSearch(no_func, x[0], step_X, step_Y)
        for i in exp.array:
            x.append(exp.array[i])
#            print x
        
        if exp.dot_min != None:
            result = 'SEARCH_SUCSESS'  
            break
    return [result, x]

if __name__ == '__main__':
    text = "%s" % unicode('Выберите функцию: ', 'utf-8')
    no_func = value.input(text, type="int", min=1, max=3)
    
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
    
    x = []
    x.append([x0_X,x0_Y])
    alpha = 10
    
#    print "x = {0}".format(x[0])
#    print "f = {0}".format(calculate.func(no_func,x[0]))
    
    first_explore = explore.ExploreSearch(no_func, x[0], step_X, step_Y)
#    print first_explore.dot_min
#    print first_explore.array.values()
    
    for i in first_explore.array:
        x.append(first_explore.array[i])
    print x
    
    if first_explore.dot_min == None:
        hand = handler(no_func, x, alpha, step_X, step_Y)
        
        if hand[0] == 'SEARCH_SUCSESS':
            x = hand[1]
    print x