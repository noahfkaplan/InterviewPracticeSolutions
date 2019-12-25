import unittest
import KthLargestElement

class KthLargestElementTests(unittest.TestCase):

    def test_returnsNone_whenInputArrayIsEmpty(self):
        array = []
        result = KthLargestElement.findKthLargest(array, 1)
        self.assertEqual(result, None)

    def test_returnsNone_whenKGreaterThanArrayLength(self):
        array = [1, 2, 3]
        result = KthLargestElement.findKthLargest(array, 4)
        self.assertEqual(result, None)

    def test_returnsKthLargestElementInTheArray_whenValidInputs(self):
        array = [3, 5, 2, 4, 6, 8]
        result = KthLargestElement.findKthLargest(array, 3)
        self.assertEqual(result, 5)
    