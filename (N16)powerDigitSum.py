import math
import time

start_time = time.perf_counter_ns()

def powDigSum(number):
    strNumber = str(number)
    sum = 0
    for i in strNumber:
        sum += int(i)
    return sum

if __name__ == '__main__':
    print(powDigSum(2**1000))
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))