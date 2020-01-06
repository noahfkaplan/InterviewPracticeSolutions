def getBonuses(performance):
    bonuses = []
    for i in range(0, len(performance)):
        bonus = 1
        if i == 0:
            bonus += 1 if performance[i] > performance[i+1] else 0
        elif i == len(performance) - 1:
            bonus += 1 if performance[i] > performance[i-1] else 0   
        else:
            bonus = 1
            bonus += 1 if performance[i] > performance[i+1] else 0
            bonus += 1 if performance[i] > performance[i-1] else 0            
        bonuses.append(bonus)

    return bonuses
