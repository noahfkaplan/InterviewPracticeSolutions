def moveZeros(array):
    for element in array:
        if element == 0:
            array.remove(element)
            array.append(element)
    
    return array
