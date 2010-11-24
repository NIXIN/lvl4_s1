# -*- coding: utf-8 -*-

def input_data(text):
    print text
    
    try:
        data = float(raw_input())
    except (TypeError, ValueError):
        print "%s" % unicode('Введены недопустимые символы. Попробуйте еще раз!', 'utf-8')
        data = input_data(text)
        
    return data

text = "%s" % unicode('Введите координату X начальной точки: ', 'utf-8')
x0_X = input_data(text)
text = "%s" % unicode('Введите координату Y начальной точки: ', 'utf-8')
x0_Y = input_data(text)

x = {}
x = {0:[x0_X,x0_Y]}

print "x = {0}    y = {1}".format(x0_X, x0_Y)
print x
print x[0]
print x[0][0]