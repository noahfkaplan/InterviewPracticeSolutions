def reverse(num):
    preserveNegative = -1 if num < 0 else 1 
    num *= preserveNegative #make number positive
    results = []
    while num > 0:
        lastDigit = num%10
        results.append(lastDigit)
        num = num - lastDigit
        num /= 10

    finalResult = 0
    count = len(results) - 1 
    for digit in results:
        finalResult += (digit * pow(10, count))
        count -= 1

    finalResult *= preserveNegative
    return finalResult


    