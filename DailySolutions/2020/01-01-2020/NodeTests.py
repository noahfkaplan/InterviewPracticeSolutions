import unittest
from Node import Node
from Node import merge

class NodeTests(unittest.TestCase):

    def test_returnsEmptyString_WhenBothLinkedListsEmpty(self):
        a = None
        b = None
        result = merge([a,b])
        self.assertEqual(str(result), '')

    def test_returnsInputtedList_WhenOneListEmpty(self):
        a = Node(1, Node(3, Node(5)))
        b = None
        result = merge([a,b])
        self.assertEqual(str(result), str(a))

    def test_returnsMergedList_WhenValidLinkedListsInputted(self):
        a = Node(1, Node(3, Node(5)))
        b = Node(2, Node(4, Node(6)))
        result = merge([a,b])
        self.assertEqual(str(result), str(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))))