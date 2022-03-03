import math
import time

start_time = time.time()

def assessIfPrime(number):
    if number==0 or number==1:
        return False
    else:
        for x in range(2, math.ceil(math.sqrt(number))+1):
            if x!=number and number%x==0:
                return False
        return True

def divisors(number):
    listOfDivisors = []
    nbOfDivisors = 0
    for n in range(1, math.ceil(math.sqrt(number)) +1):
        if number%n==0:
            listOfDivisors.append(n)
            if number/n == n:
                nbOfDivisors += 1
            else:
                nbOfDivisors += 2
                listOfDivisors.append(number/n)
    return nbOfDivisors, listOfDivisors

def sumOfNaturalNumbers(n):
    sumOfNaturalNumbers = 0
    for n in range(n):
        sumOfNaturalNumbers += n
    return sumOfNaturalNumbers

def hDTN(divisibility):
    nbOfDivisors = 0
    i = 0
    while nbOfDivisors < divisibility:
        i += 1
        sum = sumOfNaturalNumbers(i)
        nbOfDivisors = divisors(sum)[0]
    return sum

if __name__ == '__main__':
    print(divisors(hDTN(500)))
    print("time elapsed: {:.2f}s".format(time.time() - start_time))