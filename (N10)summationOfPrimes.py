import math
import time

start_time = time.perf_counter_ns()

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
            sum += i
    return sum

if __name__ == '__main__':
    print(summationOfPrimes(40))
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))
