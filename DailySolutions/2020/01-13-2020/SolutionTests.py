import unittest
import Solution

class SolutionTests(unittest.TestCase):

    def test_sortColorsDoesNotChangeList_WhenEmptyListInputted(self):
        colorsList = []
        Solution.Solution().sortColors(colorsList)
        self.assertEqual(colorsList, [])

    def test_sortColorsSortsList_WhenSortedListInputted(self):
        colorsList = [0, 0, 1, 2, 2]
        Solution.Solution().sortColors(colorsList)
        self.assertEqual(colorsList, [0, 0, 1, 2, 2])
    
    def test_sortColorsSortsList_WhenListContainsOneColor(self):
        colorsList = [0, 0, 0, 0]
        Solution.Solution().sortColors(colorsList)
        self.assertEqual(colorsList, [0, 0, 0, 0,])

    def test_sortColorsSortsList_WhenListContainsAllColors(self):
        colorsList = [1, 0, 0, 2]
        Solution.Solution().sortColors(colorsList)
        self.assertEqual(colorsList, [0, 0, 1, 2])
