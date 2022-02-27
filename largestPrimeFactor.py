import math

def largestPrimeFactor(number):
    largestPrimeFactor = number
    for y in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % y == 0:
            divisor = number / y
            if assessIfPrime(y):
                largestPrimeFactor = y
            if assessIfPrime(divisor):
                largestPrimeFactor = divisor
    print(largestPrimeFactor)