import unittest
from Solution import Solution

class SolutionTests(unittest.TestCase):
    def test_returnsEmptyArray_WhenEmptyArrayInputted(self):
        array = []
        result = Solution().findDisappearedNumbers(array)
        self.assertEqual([], result)
        
    def test_returnsEmptyArray_WhenAllValuesFrom1ToNInputted(self):
        array = [1, 2, 3, 4]
        result = Solution().findDisappearedNumbers(array)
        self.assertEqual([], result)

    def test_returns1ToN_WhenNoValuesFrom1ToNInputted(self):
        array = [5, 6, 7, 8]
        result = Solution().findDisappearedNumbers(array)
        self.assertEqual([1, 2, 3, 4], result)

    def test_returnsMissingNumbers_WhenSomeValuesInputtedFrom1ToN(self):
        array = [4, 6, 2, 6, 7, 2, 1]
        result = Solution().findDisappearedNumbers(array)
        self.assertEqual([3, 5], result)