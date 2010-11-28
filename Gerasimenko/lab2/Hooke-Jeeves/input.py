# -*- coding: utf-8 -*-

def input(text):
    print text
    
    try:
        if text == 'Выберите функцию: ':
            value = int(raw_input())
            if value < 1 or value > 3:
                raise ValueError
        else:
            value = float(raw_input())
    except (TypeError, ValueError):
        print "%s" % unicode('Введены неверные значения. Попробуйте еще раз!', 'utf-8')
        value = input(text)
        
    return value