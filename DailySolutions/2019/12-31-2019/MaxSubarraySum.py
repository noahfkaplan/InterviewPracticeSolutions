def max_subarray_sum(array):
    if len(array) == 0:
        return None
    maxSum = array[0]
    currentSum = 0
    for value in array:
        currentSum += value
        if currentSum < 0:
            currentSum = value
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum