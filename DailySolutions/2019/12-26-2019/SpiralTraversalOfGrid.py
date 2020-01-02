def matrix_spiral_print(matrix):
    if len(matrix[0]) == 0:
        return
    
    visitedPositions = []
    outputArray = []
    currentPosition = (0, 0)

    visitedPositions.append(currentPosition)
    outputArray.append(matrix[currentPosition[0]][currentPosition[1]])

    while len(outputArray) < len(matrix) * len(matrix[0]):
        #move right
        while currentPosition[0] < len(matrix[0])-1 and not checkIfInArray(visitedPositions, (currentPosition[0]+1,currentPosition[1])):
            currentPosition = (currentPosition[0] + 1, currentPosition[1])
            outputArray.append(matrix[currentPosition[1]][currentPosition[0]])
            visitedPositions.append((currentPosition[0], currentPosition[1]))
        #move down
        while currentPosition[1] < len(matrix)-1 and not checkIfInArray(visitedPositions, (currentPosition[0], currentPosition[1]+1)):
            currentPosition = (currentPosition[0], currentPosition[1] + 1)
            outputArray.append(matrix[currentPosition[1]][currentPosition[0]])
            visitedPositions.append((currentPosition[0], currentPosition[1]))
        #move left
        while currentPosition[0] != 0 and not checkIfInArray(visitedPositions, (currentPosition[0]-1, currentPosition[1])):
            currentPosition = (currentPosition[0] - 1, currentPosition[1])
            outputArray.append(matrix[currentPosition[1]][currentPosition[0]])
            visitedPositions.append((currentPosition[0], currentPosition[1]))
        #move up
        while currentPosition[1] != 0 and not checkIfInArray(visitedPositions, (currentPosition[0], currentPosition[1]-1)):
            currentPosition = (currentPosition[0], currentPosition[1] - 1)
            outputArray.append(matrix[currentPosition[1]][currentPosition[0]])
            visitedPositions.append((currentPosition[0], currentPosition[1]))
    return outputArray

def checkIfInArray(array, value): 
    try: 
        array.index(value)
        return True
    except:
        return False
