def assessIfPrime(number):
    for x in range(math.ceil(math.sqrt(number))+1):
        if x!=0 and x!=1 and number%x==0:
            return False
        else:
            continue
    return True

def assessIfCoprime(n, m):
    return math.gcd(n, m) == 1

def phiFunction(number):
    phi = 0
    for n in range(number):
        if assessIfCoprime(n, number):
            phi += 1
    return phi

"""""""""
Shitty Non-Optimal Method with n^2

def totientMax(number):
    totientMax = 0
    totientMaxRatio = 0
    for n in range(1, number + 1):
        ratio = n / phiFunction(n)
        if totientMaxRatio < ratio:
            totientMaxRatio = ratio
            totientMax = n
    return totientMax
"""""""""

#Epic Method

def totientMax(number):
    totientMax = 1
    for n in range(1, number+1):
        if assessIfPrime(n):
            product = totientMax*n
            if product > number:
                return totientMax
            else:
                totientMax = product

def primeFactors(number):
    primeFactors = []
    for n in range(1, math.ceil(math.sqrt(number))):
        if number%n == 0:
            if assessIfPrime(n):
                primeFactors.append(n)
            if assessIfPrime(number/n):
                primeFactors.append(number/n)
    return primeFactors