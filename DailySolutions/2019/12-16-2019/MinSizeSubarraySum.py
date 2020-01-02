def minSubArrayLen(nums, s):
    minLength = -1
    subarray = nums.copy()
    for i in nums:
        subarray.remove(i)
        if i > s:
            continue
        elif i == s:
            minLength = 1
            break
        else:        
            currentLength = 1
            currentSum = i
        for j in subarray:
            currentLength += 1
            currentSum += j
            if currentSum == s:
                if currentLength < minLength or minLength == -1:
                    minLength = currentLength
                break
            if currentSum > s:
                break
    return minLength