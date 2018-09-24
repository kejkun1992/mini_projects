# -*- coding: utf-8 -*-

import unittest
import multi


class TestMulti(unittest.TestCase):
    def test_list_to_str(self):
        self.assertEqual(multi.list_to_str([1, 2, 3]), '1*2*3')
        
if __name__ == '__main__':
    unittest.main()