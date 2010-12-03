# -*- coding: utf-8 -*-

def input(text, **params):
    type = params.pop("type", None)
    min = params.pop("min", None)
    max = params.pop("max", None)
    
    print text
     
    try:
        if type == "int":
            value = int(raw_input())
        elif type == "float":
            value = float(raw_input())
        elif type == "str":
            value = raw_input()
        else:
            raise TypeError
            
        if min != None and value < min:
            raise ValueError
        if max != None and value > max:
            raise ValueError
        
    except (TypeError, ValueError):
        print "%s" % unicode('Введены неверные значения. Попробуйте еще раз!', 'utf-8')
        value = input(text, type=type, min=min, max=max)
    
    return value
 
       
#text = "Input data:"    
#test_int = input(text, type="int", min=1, max=3)
#print "test_int = {0}".format(test_int)

#test_float = input(text="Input float:", type="float")
#print "test_float = {0}".format(test_float)

#test_str = input(text="Input str:", type="str")
#print "test_str = {0}".format(test_str)