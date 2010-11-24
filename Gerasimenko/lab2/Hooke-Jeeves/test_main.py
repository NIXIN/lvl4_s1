# -*- coding: utf-8 -*-

import unittest
from main import func
from main import incr_X, decr_X
from main import incr_Y, decr_Y 

class TestFunc(unittest.TestCase):
    def test_func1(self):
        x = [1,1] 
        self.assertEqual(17, func(1, x))
        
    def test_func2(self):
        x = [1,1] 
        self.assertEqual(0, func(2, x))
        
    def test_func3(self):
        x = [1,1] 
        self.assertEqual(0, func(3, x))
        
class TestX(unittest.TestCase):
    def test_incrX(self):
        x = [1,1]
        stepX = 1
        self.assertEqual([2,1], incr_X(x,stepX))
        
    def test_decrX(self):
        x = [1,1]
        stepX = 1
        self.assertEqual([0,1], decr_X(x,stepX))
        
class TestY(unittest.TestCase):
    def test_incrY(self):
        x = [1,1]
        stepY = 1
        self.assertEqual([1,2], incr_Y(x,stepY))
        
    def test_decrY(self):
        x = [1,1]
        stepY = 1
        self.assertEqual([1,0], decr_Y(x,stepY))