def first_missing_positive(array):
    array = list(filter(lambda value: value > 0, array))
    if not array:
        return None
    storage = [0] * len(array)    
    for value in array:
        if value <= len(array):
            storage[value - 1] = 1
            
    try:
        return storage.index(0) + 1
    except:
        return len(storage) + 1