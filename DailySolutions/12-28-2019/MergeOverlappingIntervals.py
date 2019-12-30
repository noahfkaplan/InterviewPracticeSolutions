def merge(array):
    sortedArray = array.copy()
    sortedArray.sort()
    merged = []
    for element in sortedArray:
        if(len(merged) == 0):
            merged.append(element)
        else:
            mergedElement = merged.pop()
            if(element[0] >= mergedElement[0] and element[0] <= mergedElement[1]):
                newElement = (mergedElement[0], max(element[1], mergedElement[1]))
                merged.append(newElement)
            else:
                merged.append(mergedElement)
                merged.append(element)
    return merged