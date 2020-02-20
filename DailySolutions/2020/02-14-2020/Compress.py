def compress(array):
    result = []
    if len(array) == 0:
        return result
    value = array[0]
    count = 1
    firstIteration = True
    result.append(value)
    for element in array:
        if firstIteration:
            firstIteration = False
            continue
        if element == value:
            count += 1            
        else:
            if count > 1:
                result.append(count)
                count = 1
            value = element
            result.append(value)
    if count > 1:
        result.append(count)
    return result



        