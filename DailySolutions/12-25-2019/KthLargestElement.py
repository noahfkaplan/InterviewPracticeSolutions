def findKthLargest(array, k):
    array.sort(reverse=True)
    if len(array) >= k:
        return array.pop(k-1)
    return None
        