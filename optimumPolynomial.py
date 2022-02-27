def nthTerm(index):
    nthTerm = 1 - index + index**2 - index**3 + index**4 - index**5 + index**6 - index**7 + index**8 - index**9 + index**10
    return nthTerm

def upToNthTerm(lastIndex):
    sequence = []
    while i<=lastIndex:
        term = nthTerm(i)
        sequence.append(term)
    return sequence

def differenceBetweenTerms(sequence):
    sequenceOfDifferences = []
    for i in range(len(sequence)):
        if i!=0:
            sequenceOfDifferences += [sequence[i] - sequence[i-1]]
        else:
            sequenceOfDifferences += [1]
    return sequenceOfDifferences