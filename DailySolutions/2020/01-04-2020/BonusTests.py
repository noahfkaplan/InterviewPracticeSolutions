import unittest
import Bonus

class BonusTests(unittest.TestCase):

    def test_ReturnsEmptyList_WhenEmptyListInputted(self):
        performance = []
        result = Bonus.getBonuses(performance)
        self.assertEqual(result, performance)

    def test_ReturnsCorrectBonus_WhenEmployeeBetterThanOneNeighbor(self):
        performance = [0, 1]
        result = Bonus.getBonuses(performance)
        self.assertEqual(result, [1, 2])
    
    def test_ReturnsCorrectBonus_WhenEmployeeBetterThanTwoNeighbors(self):
        performance = [0, 1, 0]
        result = Bonus.getBonuses(performance)
        self.assertEqual(result, [1, 3, 1])

    def test_ReturnsCorrectBonus_WhenPerformanceContainsAllScenarios(self):
        performance = [1, 2, 3, 2, 3, 5, 1]
        result = Bonus.getBonuses(performance)
        self.assertEqual(result, [1, 2, 3, 1, 2, 3, 1])