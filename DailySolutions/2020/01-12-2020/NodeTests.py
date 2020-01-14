import unittest
import Node

class NodeTests(unittest.TestCase):

    def test_traverseReturnsEmptyList_WhenNodeIsNone(self):
        a = None
        nodeList = []
        Node.traverse(a, nodeList)
        self.assertEqual(nodeList, []) 

    def test_traverseReturnsListOfNodes_WhenNodesHaveleftChildrenOnly(self):
        a = Node.Node(0)
        a.left = Node.Node(1)
        a.left.left = Node.Node(2)
        nodeList = []
        Node.traverse(a, nodeList)
        self.assertEqual(len(nodeList), 3) 

    def test_traverseReturnsListOfNodes_WhenNodesHaverightChildrenOnly(self):
        a = Node.Node(0)
        a.right = Node.Node(1)
        a.right.right = Node.Node(2)
        nodeList = []
        Node.traverse(a, nodeList)
        self.assertEqual(len(nodeList), 3) 


    def test_traverseReturnsListOfNodes_WhenNodesHaveleftandrightChildren(self):
        a = Node.Node(0)
        a.left = Node.Node(1)
        a.right = Node.Node(2)
        nodeList = []
        Node.traverse(a, nodeList)
        self.assertEqual(len(nodeList), 3) 

    def test_countUnivalSubtreesReturnsZero_WhenRootNone(self):
        a = None
        result = Node.countUnivalSubtrees(a)
        self.assertEqual(result, 0)

    def test_countUnivalSubtreesReturnsOne_WhenRootHasNoChildren(self):
        a = Node.Node(0)
        result = Node.countUnivalSubtrees(a)
        self.assertEqual(result, 1)

    def test_countUnivalSubtreesReturnsNumberOfChildlessNodes_WhenNoDuplicateValues(self):
        a = Node.Node(0)
        a.left = Node.Node(1)
        a.right = Node.Node(2)
        a.right.left = Node.Node(3)
        a.right.right = Node.Node(4)
        a.right.left.left = Node.Node(5)
        a.right.left.right = Node.Node(6)
        result = Node.countUnivalSubtrees(a)
        self.assertEqual(result, 4)

    def test_countUnivalSubtreesReturnsNumberOfUnivalTrees_WhenValidTree(self):
        a = Node.Node(0)
        a.left = Node.Node(1)
        a.right = Node.Node(0)
        a.right.left = Node.Node(1)
        a.right.right = Node.Node(0)
        a.right.left.left = Node.Node(1)
        a.right.left.right = Node.Node(1)
        result = Node.countUnivalSubtrees(a)
        self.assertEqual(result, 5)

