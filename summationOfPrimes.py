def assessIfPrime(number):
    if number==0 or number==1:
        return False
    else:
        for x in range(2, math.ceil(math.sqrt(number))+1):
            if x!=number and number%x==0:
                return False
        return True

def summationOfPrimes(underN):
    sum = 0
    for i in range(underN+1):
        if assessIfPrime(i):
            print(i)
            sum += i
    print(sum)
