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

def largestPrimeFactor(number):
    largestPrimeFactor = number
    for y in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % y == 0:
            divisor = number / y
            if assessIfPrime(y):
                largestPrimeFactor = y
            if assessIfPrime(divisor):
                largestPrimeFactor = divisor
    return largestPrimeFactor

if __name__ == '__main__':
    print(largestPrimeFactor(600851475143))
    print("time elapsed: {:.2f}s".format(time.time() - start_time))