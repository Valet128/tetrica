import unittest

from solution import *

class IntervalsTest(unittest.TestCase):
    def test_appearance(self):

        self.assertEqual(appearance(tests[0]['intervals']), tests[0]['answer'])
        self.assertEqual(appearance(tests[1]['intervals']), tests[1]['answer'])
        self.assertEqual(appearance(tests[2]['intervals']), tests[2]['answer'])

    def test_values(self):
        self.assertRaises(TypeError, appearance, {'lesson': ["1594663200", 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]})
        self.assertRaises(TypeError, appearance, {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 15946633.89, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]})
        self.assertRaises(TypeError, appearance, {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, [1234,124], 1594666473]})
        self.assertRaises(ValueError, appearance, {'lessons': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]})
        self.assertRaises(ValueError, appearance, {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor4': [1594663290, 1594663430, 1594663443, 1594666473]})
        self.assertRaises(ValueError, appearance, {'lesson': [1594663200, 1594666800],
             'pupilf': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]})
     

if __name__ == "__main__":
    unittest.main()