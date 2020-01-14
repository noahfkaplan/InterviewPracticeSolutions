import Node

a = Node.Node(0)
a.left = Node.Node(1)
a.right = Node.Node(0)
a.right.left = Node.Node(1)
a.right.right = Node.Node(0)
a.right.left.left = Node.Node(1)
a.right.left.right = Node.Node(1)

print(Node.countUnivalSubtrees(a))
