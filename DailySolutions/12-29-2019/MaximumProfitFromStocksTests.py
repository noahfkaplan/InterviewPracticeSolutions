import unittest
import MaximumProfitFromStocks

class MaximumProfitFromStocksTests(unittest.TestCase):

    def test_returnsNone_WhenInputtedArrayEmpty(self):
        array = []
        result = MaximumProfitFromStocks.buy_and_sell(array)
        self.assertEqual(result, None)

    def test_returnsNone_WhenInputtedArrayContains1Value(self):
        array = []
        result = MaximumProfitFromStocks.buy_and_sell(array)
        self.assertEqual(result, None)

    def test_returnsDiffBetweenMaxAndMinValue_WhenInputtedArrayAscending(self):
        array = [0, 5, 15, 40]
        result = MaximumProfitFromStocks.buy_and_sell(array)
        self.assertEqual(result, 40)
    
    def test_returnsDiffBetweenClosestValues_WhenInputtedArrayDescending(self):
        array = [40, 15, 5, 0]
        result = MaximumProfitFromStocks.buy_and_sell(array)
        self.assertEqual(result, -5)

    def test_returnsMaxProfit_WhenInputtedArrayValid(self):
        array = [9, 11, 8, 5, 7, 10]
        result = MaximumProfitFromStocks.buy_and_sell(array)
        self.assertEqual(result, 5)