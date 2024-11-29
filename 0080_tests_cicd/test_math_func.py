import unittest
import math_func

#python3 -m unittest test_math_func.py
#python3 test_math_func.py  - works if we have  __name__=="__main"

class TestMathFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_func.add(2,5),7)
        self.assertEqual(math_func.add(-1,1),0)
        self.assertEqual(math_func.add(-1,-1),-2)

    def test_substract(self):
        self.assertEqual(math_func.substract(2,5),-3)
        self.assertEqual(math_func.substract(-1,1),-2)
        self.assertEqual(math_func.substract(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(math_func.multiply(2,5),10)
        self.assertEqual(math_func.multiply(-1,1),-1)
        self.assertEqual(math_func.multiply(-1,-1),1)
        
    def test_divide(self):
        self.assertEqual(math_func.divide(2,5),0.4)
        self.assertEqual(math_func.divide(-1,1),-1)
        self.assertEqual(math_func.divide(-1,-1),1)
        self.assertEqual(math_func.divide(10,2),5)
        #self.assertEqual(math_func.divide(10,0),5)
        #to catch raides error
        self.assertRaises(ValueError,math_func.divide,10,0)



if __name__ == '__main__':
    unittest.main()