import unittest
import ex1

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(ex1.add(10, 5), 15)
        self.assertEqual(ex1.add(-1, 1), 0)
        self.assertEqual(ex1.add(-1, -1),-2)
        self.assertEqual(ex1.add(10, 5), 15)
     
    def test_subtract(self):
        self.assertEqual(ex1.subtract(10, 5), 5)
        self.assertEqual(ex1.subtract(-1, 1), -2)
        self.assertEqual(ex1.subtract(-1, -1), 0)
        self.assertEqual(ex1.subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(ex1.multiply(10, 5), 50)
        self.assertEqual(ex1.multiply(-1, 1), -1)
        self.assertEqual(ex1.multiply(-1, -1), 1)
        self.assertEqual(ex1.multiply(10, 5), 50)
         
    def test_divide(self):
        self.assertEqual(ex1.divide(10, 2), 5)
        self.assertEqual(ex1.divide(3, 1), 3)
        self.assertEqual(ex1.divide(-1, -1), 1)
        self.assertEqual(ex1.divide(10, 5), 2)

        with self.assertRaises(ValueError):
            ex1.divide(10, 0)

if __name__ == '__main__':
    unittest.main()