import unittest
import Node

class NodeTests(unittest.TestCase):

    def test_valuesAtHeightReturnsEmptyArray_WhenHeightIsZero(self):
        a = Node.Node(1)
        result = Node.valuesAtHeight(a, 0)
        self.assertEqual(result, []) 


    def test_valuesAtHeightReturnsEmptyArray_WhenMaxHeightLessThanHeight(self):
        a = Node.Node(1)
        result = Node.valuesAtHeight(a, 2)
        self.assertEqual(result, []) 

    def test_valuesAtHeightReturnsCorrectValues_WhenOneValueAtHeight(self):
        a = Node.Node(1)
        a.left = Node.Node(2)
        result = Node.valuesAtHeight(a, 2)
        self.assertEqual(result, [2]) 

    def test_valuesAtHeightReturnsCorrectValues_WhenMoreThanOneValueAtHeight(self):
        a = Node.Node(1)
        a.left = Node.Node(2)
        a.right = Node.Node(3)
        a.left.left = Node.Node(4)
        a.left.right = Node.Node(5)
        a.right.right = Node.Node(7)
        result = Node.valuesAtHeight(a, 3)
        self.assertEqual(result, [4, 5, 7])

    def test_valuesAtHeightReturnsCorrectValues_WhenAllPossibleValuesAtHeight(self):
        a = Node.Node(1)
        a.left = Node.Node(2)
        a.right = Node.Node(3)
        a.left.left = Node.Node(4)
        a.left.right = Node.Node(5)
        a.right.right = Node.Node(7)
        a.right.left = Node.Node(8)
        result = Node.valuesAtHeight(a, 3)
        self.assertEqual(result, [4, 5, 8, 7])

    def test_getCombinationsReturnsEmptySet_WhenHeightIs0(self):
        height = 0
        expectedCombinations = []
        result = Node.getCombinations(height)
        self.assertEqual(result, expectedCombinations)

    def test_getCombinationsReturnsCorrectSets_WhenHeightIs4(self):
        height = 4
        expectedCombinations = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], 
                                [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], 
                                [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], 
                                [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
        result = Node.getCombinations(height)
        self.assertEqual(result, expectedCombinations)

    def test_getCombinationsReturnsCorrectSets_WhenHeightIs2(self):
        height = 2
        expectedCombinations = [[0, 0], [0, 1], 
                                [1, 0], [1, 1]]
        result = Node.getCombinations(height)
        self.assertEqual(result, expectedCombinations)