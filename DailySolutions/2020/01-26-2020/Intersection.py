def getIntersection(array1, array2):
    result = []
    if not array1 or not array2:
        return result
    for value1 in array1:
        if value1 in array2 and value1 not in result:
            result.append(value1)
    return result