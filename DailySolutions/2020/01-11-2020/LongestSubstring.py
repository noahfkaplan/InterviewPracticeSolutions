def longest_substring_with_k_distinct_characters(s, k):
    longestSubstring = 0
    activeSubstring = 0
    activeCharacters = [] #array of tuples (character, newestOccurance)

    for characterIndex in range(0, len(s)):
        index = containsCharacter(activeCharacters, s[characterIndex]) 
        if index >= 0: #active substring grows because no new unique character
            characterToBeUpdated = activeCharacters.pop(index)
            activeCharacters.append((characterToBeUpdated[0], characterIndex))
            activeSubstring += 1
        elif len(activeCharacters) < k: #active string continues because less than K unique characters so far
            activeCharacters.append((s[characterIndex], characterIndex))
            activeSubstring += 1
        else:
            longestSubstring = max(longestSubstring, activeSubstring)
            #since we append new characters that are used, the earliest index will be the longest ago used
            removedCharacter = activeCharacters.pop(0)           
            #active substring length = difference between current index and newest occurance of removed character
            activeSubstring = characterIndex - removedCharacter[1]
            activeCharacters.append((s[characterIndex], characterIndex)) 

    longestSubstring = max(longestSubstring, activeSubstring)
    return longestSubstring


def containsCharacter(array, character):
    for element in array:    
        if(element[0] == character):
            return array.index(element)
    return -1