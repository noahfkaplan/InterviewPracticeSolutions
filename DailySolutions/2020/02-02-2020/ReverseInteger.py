def reverse(num):
    preserveNegative = -1 if num < 0 else 1 
    num *= preserveNegative #make number positive
    
    finalResult = 0
    while num > 0:
        lastDigit = num%10
        finalResult *= 10
        finalResult += lastDigit
        num = num - lastDigit
        num /= 10

    finalResult *= preserveNegative
    return finalResult


    