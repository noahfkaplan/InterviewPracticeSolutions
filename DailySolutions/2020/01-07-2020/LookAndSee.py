def LookAndSee(n):
    if n < 0:
        return ''
    currentValue = '1'
    for i in range(0, n):
        newValue = ''
        previousCharacter = None
        consectutiveCharacters = 1
        for index in range(0, len(currentValue)):
            if previousCharacter == None:
                previousCharacter = currentValue[index]
                continue
            elif currentValue[index] == previousCharacter:
                consectutiveCharacters += 1
            else:
                newValue += str(consectutiveCharacters) + previousCharacter
                previousCharacter = currentValue[index]
                consectutiveCharacters = 1
        
        newValue += str(consectutiveCharacters) + previousCharacter
        currentValue = newValue
    return currentValue
