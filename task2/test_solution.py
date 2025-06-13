import unittest

from solution import *

class BeastsTest(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(main(global_url[0]), "END")
        
    def test_values(self):
        self.assertEqual(global_url[0], "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")
        self.assertRaises(ValueError, main, "https://ru.wikipedia.org/wiki/Категория:Животные_не_по_алфавиту")
        
        

if __name__ == "__main__":
    unittest.main()