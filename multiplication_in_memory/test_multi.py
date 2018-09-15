# -*- coding: utf-8 -*-

import unittest
import multi


class TestMulti(unittest.TestCase):
    def test_list_to_str(self):
        self.assertEqual(multi.list_to_str([1, 2, 3]), '1*2*3')
        
    def test_random_operation1(self):
        self.assertEqual(len(multi.random_operation(1, 3)), 5)
        
    def test_random_operation2(self):
        self.assertEqual(len(multi.random_operation(3, 4)), 15)
        
if __name__ == '__main__':
    unittest.main()