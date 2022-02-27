def assessIfPrime(number):
    for x in range(math.ceil(math.sqrt(number))+1):
        if x!=0 and x!=1 and number%x==0:
            return False
        else:
            continue
    return True

def smallestMultiple(upToWhatNumber):
    smallestMultiple = 1
    for i in range(upToWhatNumber-1):
        if assessIfPrime(i):
            smallestMultiple = smallestMultiple*i
        elif smallestMultiple%i!=0:
            smallestMultiple
