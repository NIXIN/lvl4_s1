# -*- coding: utf-8 -*-

import func as calculate
import explore_search as explore
import input as value


if __name__ == '__main__':
    text = "%s" % unicode('Выберите функцию: ', 'utf-8')
    vib_func = value.input(text)
    
    
    text = "%s" % unicode('Введите координату x1 начальной точки: ', 'utf-8')
    x0_X = value.input(text)
    text = "%s" % unicode('Введите координату x2 начальной точки: ', 'utf-8')
    x0_Y = value.input(text)
    
    text = "%s" % unicode('Введите шаг по координате X: ', 'utf-8')
    step_X = value.input(text)
    text = "%s" % unicode('Введите шаг по координате Y: ', 'utf-8')
    step_Y = value.input(text)
    
    x = {}
    x = {0:[x0_X,x0_Y]}
    
    print "x = {0}".format(x[0])
    print "f = {0}".format(calculate.func(vib_func,x[0]))
    exp = explore.ExploreSearch(vib_func, x[0], step_X, step_Y)
    
    print exp.array.values()
    
    