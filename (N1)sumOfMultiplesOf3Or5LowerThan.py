import math
import time

start_time = time.perf_counter_ns()

def sumOfMultiplesOf3or5LowerThan(number):
    sum = 0
    for x in range(number):
    #loop through the numbers lower than and add if divisible by 3 or 5
        if x%3==0 or x%5==0:
            sum += x
    return sum

if __name__ == '__main__':
    print(sumOfMultiplesOf3or5LowerThan(1000))
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))