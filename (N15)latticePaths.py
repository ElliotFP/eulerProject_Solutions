import math
import time

start_time = time.perf_counter_ns()

def latticePaths(squareGrid):
    n = 2*(squareGrid)
    k = (squareGrid)
    denominator = math.factorial(n)
    numerator = math.factorial(k)**2
    return denominator/numerator

if __name__ == '__main__':
    print(latticePaths(20))
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))