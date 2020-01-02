def witnesses(queue):
    numberOfWitnesses = 0
    aheadInQueue = queue.copy()
    for height in queue:
        aheadInQueue.remove(height)
        numberOfWitnesses += 1 #will be removed if anyone ahead in queue is taller
        for aheadHeights in aheadInQueue:
            if(height <= aheadHeights):
                numberOfWitnesses -= 1
                break
    return numberOfWitnesses
        
