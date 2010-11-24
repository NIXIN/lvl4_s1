# -*- coding: utf-8 -*-

import unittest
from main import func

class TestFunc(unittest.TestCase):
    
    def test_func1(self):
        x = [2,2] 
        self.assertEqual(74, func(1, x))