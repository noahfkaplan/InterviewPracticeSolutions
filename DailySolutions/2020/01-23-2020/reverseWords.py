def reverse(string):
    words = string.split()
    updatedSentence = ''
    for word in words:
        updatedSentence += word[::-1] + ' '
    updatedSentence = updatedSentence[:len(updatedSentence) - 1] #remove trailing space
    return updatedSentence
