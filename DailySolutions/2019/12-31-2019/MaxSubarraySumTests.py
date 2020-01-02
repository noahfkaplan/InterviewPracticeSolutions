import unittest
import MaxSubarraySum

class MaxSubarraySumTests(unittest.TestCase):

    def test_ReturnsNone_WhenInputtedArrayEmpty(self):
        array = []
        result = MaxSubarraySum.max_subarray_sum(array)
        self.assertEqual(result, None)

    def test_ReturnsFirstValue_WhenInputtedArrayHasOneValue(self):
        array = [5]
        result = MaxSubarraySum.max_subarray_sum(array)
        self.assertEqual(result, array[0])

    def test_ReturnsSumOfAllValues_WhenAllValuesPositive(self):
        array = [1, 2, 3, 4]
        result = MaxSubarraySum.max_subarray_sum(array)
        self.assertEqual(result, sum(array))

    def test_ReturnsLargestNegativeNumber_WhenAllValuesNegative(self):
        array = [-1, -2, -3, -4]
        result = MaxSubarraySum.max_subarray_sum(array)
        self.assertEqual(result, array[0])

    def test_ReturnsLargestSum_WhenValuesPositiveAndNegative(self):
        array = [34, -50, 42, 14, -5, 86]
        result = MaxSubarraySum.max_subarray_sum(array)
        self.assertEqual(result, 137)