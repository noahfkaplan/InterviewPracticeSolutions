class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
    values = []
    combinations = getCombinations(height - 1)
    for combination in combinations:
        nextNode = root
        for direction in combination:
            if not nextNode:
                return 
            nextNode = nextNode.left if direction == 0 else nextNode.right
        if nextNode:
            values.append(nextNode.value)
    return values

def getCombinations(height):
    combinations = []
    for count in range(0, height * height):
        tempCount = count
        currentCombination = [0] * height
        currentIndex = height - 1

        while tempCount > 0:
            if tempCount % 2 == 1:
                currentCombination[currentIndex] = 1
                currentIndex -= 1
                tempCount = (tempCount - 1)/2
            else:
                currentIndex -= 1
                tempCount = tempCount/2
        if currentCombination: #handle the height of 0 case
            combinations.append(currentCombination)
    
    return combinations



