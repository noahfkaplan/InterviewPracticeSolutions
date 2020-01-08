import unittest
import FirstMissingInteger

class FirstMissingIntegerTests(unittest.TestCase):

    def test_ReturnsNone_WhenEmptyArrayInputted(self):
        array = []
        result = FirstMissingInteger.first_missing_positive(array)
        self.assertEqual(result, None)

    def test_ReturnsNone_WhenAllValuesNegative(self):
        array = [-1, -2, -3]
        result = FirstMissingInteger.first_missing_positive(array)
        self.assertEqual(result, None)

    def test_ReturnsOne_WhenAllPositiveValuesAndOneNotInputted(self):
        array = [2, 3, 4]
        result = FirstMissingInteger.first_missing_positive(array)
        self.assertEqual(result, 1)

    def test_ReturnsLengthPlus1_WhenAllPositiveFromOneToLength(self):
        array = [1, 2, 3]
        result = FirstMissingInteger.first_missing_positive(array)
        self.assertEqual(result, 4)
   
    def test_ReturnsMinumumPositiveValue_WhenValuesDecreasing(self):
        array = [4, 2, 1]
        result = FirstMissingInteger.first_missing_positive(array)
        self.assertEqual(result, 3)

    def test_ReturnsMinumumPositiveValue_WhenPositiveAndNegativeValuesInputted(self):
        array = [3, 4, -1, 1]
        result = FirstMissingInteger.first_missing_positive(array)
        self.assertEqual(result, 2)