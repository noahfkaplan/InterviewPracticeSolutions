import unittest
import MoveZeros

class MoveZerosTests(unittest.TestCase):

    def test_returnsEmptyArray_WhenInputtedArrayIsEmpty(self):
        array = []
        result = MoveZeros.moveZeros(array)
        self.assertEqual(result, array)

    def test_returnsUnchangedArray_WhenInputtedArrayHasNoZeros(self):
        array = [2, 1, 3, 4]
        result = MoveZeros.moveZeros(array)
        self.assertEqual(result, array)

    def test_returnsArrayWithZerosAtTheEnd_WhenInputtedArrayHasZeros(self):
        array = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
        expectedResult =  [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]