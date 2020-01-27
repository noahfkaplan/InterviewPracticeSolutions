import unittest
import Intersection

class IntersectionTests(unittest.TestCase):

    def test_IntersectionReturnsEmptyArray_WhenBothInputtedArrayEmpty(self):
        a = []
        b = []
        result = Intersection.getIntersection(a, b)
        self.assertEqual(result, [])

    def test_IntersectionReturnsEmptyArray_WhenOneInputtedArrayEmpty(self):
        a = [1, 2, 3, 4]
        b = []
        result = Intersection.getIntersection(a, b)
        self.assertEqual(result, [])
    
    def test_IntersectionReturnsEmptyArray_WhenInputtedArraysHaveNoIntersection(self):
        a = [1, 3, 5, 7]
        b = [2, 4, 6, 8]
        result = Intersection.getIntersection(a, b)
        self.assertEqual(result, [])

    def test_IntersectionReturnsOneElement_WhenInputtedArraysHaveOneIntersection(self):
        a = [1, 3, 5, 7]
        b = [2, 3, 4, 6]
        result = Intersection.getIntersection(a, b)
        self.assertEqual(result, [3])

    def test_IntersectionReturnsMultipleElements_WhenInputtedArraysHaveMultipleIntersections(self):
        a = [1, 3, 5, 7]
        b = [2, 3, 4, 5]
        result = Intersection.getIntersection(a, b)
        self.assertEqual(result, [3, 5])

    def test_IntersectionReturnsUniqueIntersections_WhenAnIntersectionExistsMultipleTimes(self):
        a = [4,9,5]
        b = [9,4,9,8,4]
        result = Intersection.getIntersection(a, b)
        self.assertEqual(result, [4, 9])
    
    def test_IntersectionReturnsInputtedArray_WhenBothArraysContainSameElements(self):
        a = [1, 2, 3, 4]
        b = [4, 3, 2, 1]
        result = Intersection.getIntersection(a, b)
        self.assertEqual(result, [1, 2, 3, 4])