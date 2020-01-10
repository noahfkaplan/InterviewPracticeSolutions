import unittest
import LookAndSee

class LookAndSeeTests(unittest.TestCase):

    def test_returnsEmptyString_WhenNegativeInput(self):
        n = -1
        result = LookAndSee.LookAndSee(n)
        self.assertEqual(result, '')
        
    def test_returnsOne_WhenZeroInputted(self):
        n = 0
        result = LookAndSee.LookAndSee(n)
        self.assertEqual(result, '1')

    def test_returnsCorectValue_WhenPositiveInput(self):
        n = 4
        result = LookAndSee.LookAndSee(n)
        self.assertEqual(result, '111221')
