from name import fullName
import unittest

class NameTest(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual('Miklos Bowling', fullName('Miklos', 'Bowling'))

    def test_missing_lastname(self):
        self.assertRaises(TypeError, fullName, 'Miklos')

    def test_numeric_args(self):
        self.assertEqual('1 2', fullName(1, 2))

if __name__ == '__main__':
    unittest.main()