# -*- coding: utf-8 -*-

import unittest
from main import func

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