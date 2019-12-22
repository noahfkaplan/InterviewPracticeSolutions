import unittest
import MinSizeSubarraySum

class MinSizeSubarraySumTests(unittest.TestCase):

    def test_returnsMinus1_WhenSumDoesNotExist(self):
        result = MinSizeSubarraySum.minSubArrayLen([1, 1, 1], 4)
        self.assertEqual(result, -1)

    def test_returnsMinus1_WhenNoValuesInArray(self):
        result = MinSizeSubarraySum.minSubArrayLen([], 1)
        self.assertEqual(result, -1)
        
    def test_returnsMinus1_WhenSumIsAlwaysExceeded(self):
        result = MinSizeSubarraySum.minSubArrayLen([1, 1, 1, 999], 4)
        self.assertEqual(result, -1)

    def test_returns1_WhenValueInArrayEqualsSum(self):
        result = MinSizeSubarraySum.minSubArrayLen([1, 4, 1], 4)
        self.assertEqual(result, 1)

    def test_returns3_When3ValuesAddedEqualsSum(self):
        result = MinSizeSubarraySum.minSubArrayLen([1, 1, 1], 3)
        self.assertEqual(result, 3)
    
    def test_returnsLowerSum_WhenMultipleSequencesEqualSum(self):
        result = MinSizeSubarraySum.minSubArrayLen([1, 1, 1, 2], 3)
        self.assertEqual(result, 2)
