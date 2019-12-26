import unittest
import SpiralTraversalOfGrid

class SpiralTraversalOfGridTests(unittest.TestCase):

    def test_ReturnsEmptyArray_WhenInputtedMatrixEmpty(self):
        matrix = [[]]
        result = SpiralTraversalOfGrid.matrix_spiral_print(matrix)
        self.assertEqual(result, None)

    def test_ReturnsSpiralSortedValues_WhenInputtedMatrixValue(self):
        matrix = [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        expectedResult = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
        result = SpiralTraversalOfGrid.matrix_spiral_print(matrix)
        self.assertEqual(result, expectedResult)