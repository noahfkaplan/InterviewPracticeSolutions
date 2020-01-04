def capacity(array):
    capacity = 0
    potentialCapacity = 0
    previousPeak = 0
    previousValley = 0
    guarenteedCapactity = 0
    for altitude in array:
        if altitude >= previousPeak:
            previousPeak = altitude
            capacity += potentialCapacity
            potentialCapacity = 0
            guarenteedCapactity = 0
            previousValley = altitude
        if altitude < previousPeak:
            potentialCapacity += previousPeak - altitude
        if altitude > previousValley and altitude < previousPeak:
            guarenteedCapactity += altitude - previousValley
        if altitude < previousValley:
            previousValley = altitude

    capacity += guarenteedCapactity   
    return capacity
    