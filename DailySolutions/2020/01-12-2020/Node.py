class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def countUnivalSubtrees(root):
    rootsList = []
    traverse(root, rootsList)
    count = 0
    for subroot in rootsList:
        subRootsList = []
        traverse(subroot, subRootsList)
        current = subRootsList[0].val
        unival = True
        for values in subRootsList:
            if values.val != current:
                unival = False
                continue
        if unival:
            count += 1
    return count
    
def traverse(root, rootList):
    if not root:
        return
    rootList.append(root)
    traverse(root.left, rootList)
    traverse(root.right, rootList)
