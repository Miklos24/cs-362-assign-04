from cube import calcCubeVolume
import unittest

class CubeTest(unittest.TestCase):
    def test_cube_int(self):
        self.assertEqual(125, calcCubeVolume(5))

    def test_cube_float(self):
        self.assertEqual(0.125, calcCubeVolume(0.5))

    def test_cube_neg(self):
        self.assertEqual(-125, calcCubeVolume(-5))

    def test_cube_value_error(self):
        self.assertRaises(TypeError, calcCubeVolume, 'fish')
    
    def test_cube_complex(self):
        self.assertEqual(-2 + 2j, calcCubeVolume(1 + 1j))

if __name__ == '__main__':
    unittest.main()