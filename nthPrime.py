def assessIfPrime(number):
    for x in range(math.ceil(math.sqrt(number))+1):
        if x!=0 and x!=1 and number%x==0:
            return False
        else:
            continue
    return True

def nthPrime(n):
    nbOfPrimes = 0
    number = 0
    while nbOfPrimes <= n:
        number += 1
        if assessIfPrime(number):
            nbOfPrimes +=1
        if nbOfPrimes == n:
            print(number)
            return nthPrime