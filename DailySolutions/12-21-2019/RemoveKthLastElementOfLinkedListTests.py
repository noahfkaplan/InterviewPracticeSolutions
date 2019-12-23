import unittest
import RemoveKthLastElementOfLinkedList
from Node import Node

class RemoveKthLastElementOfLinkedListTests(unittest.TestCase):

    def test_returnsNone_WhenInputListIsNone(self):
        head = None
        result = RemoveKthLastElementOfLinkedList.remove_kth_from_linked_list(head, 1)
        self.assertIsNone(head)

    def test_returnsInputList_WhenListShorterThanKElements(self):
        head = Node(1)
        result = RemoveKthLastElementOfLinkedList.remove_kth_from_linked_list(head, 2)
        self.assertEqual(str(result), str(head))
    
    def test_returnsListWithoutKthLastElement_WhenListLongerThanKElements(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        expectedResult = Node(1, Node(2, Node(4, Node(5))))
        result = RemoveKthLastElementOfLinkedList.remove_kth_from_linked_list(head, 3)
        self.assertEqual(str(result), str(expectedResult))