import unittest
import MaxProductOfThree

class MaxProductOfThreeTests(unittest.TestCase):

    def test_returnsNone_WhenNoElementsInArray(self):
        array = []
        result = MaxProductOfThree.maximum_product_of_three(array)
        self.assertEqual(result, None)
    def test_returnsNone_WhenLessThan3Elements(self):
        array = [1, 2]
        result = MaxProductOfThree.maximum_product_of_three(array)
        self.assertEqual(result, None)
    def test_returnsProductOfAllElement_WhenExactly3Elements(self):
        array = [2, 2, 3]
        result = MaxProductOfThree.maximum_product_of_three(array)
        self.assertEqual(result, 12)
    def test_returnsLargestProduct_WhenNoNegativeValuesInArray(self):
        array = [2, 2, 3, 3]
        result = MaxProductOfThree.maximum_product_of_three(array)
        self.assertEqual(result, 18)
    def test_returnsLargestProduct_WhenSomeNegativeValuesInArray(self):
        array = [-4, -4, 2, 8]
        result = MaxProductOfThree.maximum_product_of_three(array)
        self.assertEqual(result, 128)
    def test_returnsLargestProduct_WhenAllNegativveValuesInArray(self):
        array = [-4, -4, -2, -8]
        result = MaxProductOfThree.maximum_product_of_three(array)
        self.assertEqual(result, -32)

    