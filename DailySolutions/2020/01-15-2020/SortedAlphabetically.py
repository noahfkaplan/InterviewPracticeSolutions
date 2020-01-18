def isSorted(words, order):
    if not words:
        return False
    previousWord = None  
    for word in words:
        if not previousWord: #handling the first iteration
            previousWord = word
            continue
        for characterIndex in range(0, len(word)):
            if characterIndex >= len(previousWord): #words have fully matched and now the new word is longer
                continue
            previousWordCharacter = previousWord[characterIndex]
            currentWordCharacter = word[characterIndex]
            if order.index(previousWordCharacter) > order.index(currentWordCharacter):
                return False
            elif order.index(previousWordCharacter) < order.index(currentWordCharacter):
                break
        if len(previousWord) > len(word) and previousWord[:len(word)] == word:
            return False
        previousWord = word
    return True