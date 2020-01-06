def buddyStrings(A, B):
    if(len(A) == len(B)):
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                newString = A[:i] + A[j] + A[i+1: j] + A[i] + A[j+1:]
                if(newString == B):
                    return True
                    


    return False