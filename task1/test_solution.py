import unittest

from solution import strict, sum_two

class TypesTest(unittest.TestCase):
    def test_decoration(self):
        decor = strict(sum_two)
        
        self.assertEqual(decor(1,2), 3)
        self.assertEqual(decor(False,True), 1)
    
    def test_values(self):
        decor = strict(sum_two)

        self.assertRaises(TypeError, decor, 3, 3.4)
        self.assertRaises(TypeError, decor, "3", 3)
        self.assertRaises(TypeError, decor, [3,4], 5)
        self.assertRaises(TypeError, decor, None, 1)
        

if __name__ == "__main__":
    unittest.main()