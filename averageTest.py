from average import average
import unittest

class TestAverage(unittest.TestCase):
    def test_int_list(self):
        self.assertEqual(2.5, average([1, 2, 3, 4]))
    
    def test_empty_list_err(self):
        self.assertRaises(ZeroDivisionError, average, [])
    
    def test_mixed_list_err(self):
        self.assertRaises(TypeError, average, [1, 'fish', None])


if __name__ == '__main__':
    unittest.main()