import unittest
import ReverseInteger

class ReverseIntegerTests(unittest.TestCase):

    def test_ReverseIntegerReturnsZero_WhenZeroInputted(self):
        num = 0
        result = ReverseInteger.reverse(num)
        self.assertEqual(result, 0)

    def test_ReverseIntegerReturnsInput_WhenInputOneDigit(self):
        num = 1
        result = ReverseInteger.reverse(num)
        self.assertEqual(result, 1)

    def test_ReverseIntegerReturnsReverse_WhenNegativeIntInputted(self):
        num = -12345
        result = ReverseInteger.reverse(num)
        self.assertEqual(result, -54321)

    def test_ReverseIntegerReturnsReverse_WhenPositiveIntInputted(self):
        num = 12345
        result = ReverseInteger.reverse(num)
        self.assertEqual(result, 54321)