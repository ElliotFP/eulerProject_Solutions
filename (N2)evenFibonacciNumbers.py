import math
import time

start_time = time.perf_counter_ns()

def evenFibonacciNumbers(number):
    x = 1
    y = 1
    sum = 0
    while y <= number:
        temp = y
        y = x + y
        x = temp
        if temp % 2 == 0:
            sum += temp
    return sum

if __name__ == '__main__':
    print(evenFibonacciNumbers(4000000))
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))
