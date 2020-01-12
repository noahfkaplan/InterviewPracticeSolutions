import Node

a = Node.Node(1)
a.left = Node.Node(2)
a.right = Node.Node(3)
a.left.left = Node.Node(4)
a.left.right = Node.Node(5)
a.right.right = Node.Node(7)
print(Node.valuesAtHeight(a, 3))