def groupAnagramWords(strings):
    results = []
    for string in strings:
        isAnagramInExistingSet = False        
        for anagramSet in results:
            isAnagram = True
            if len(string) != len(anagramSet[0]):
                continue
            for stringCharacter in string:
                containsCharacter = False
                for anagramStringCharacter in anagramSet[0]:
                    if anagramStringCharacter == stringCharacter:
                        containsCharacter = True
                if not containsCharacter:
                    isAnagram = False
            if isAnagram:
                anagramSet.append(string)
                isAnagramInExistingSet = True
                break
            
        if not isAnagramInExistingSet:
            results.append([string])
    return results
