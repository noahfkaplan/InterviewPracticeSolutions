def buy_and_sell(array):
    if len(array) < 2:
        return None
        
    maxProfit = array[1] - array[0]
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            maxProfit = max(maxProfit, array[j] - array[i])
    return maxProfit
