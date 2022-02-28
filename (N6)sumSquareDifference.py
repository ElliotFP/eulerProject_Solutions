import math
import time

start_time = time.perf_counter_ns()

def sumSquareDifference(firstNNumbers):
    sumOfFirstNNumbers = 0
    sumOfSquares = 0
    for i in range(firstNNumbers+1):
        sumOfFirstNNumbers += i
        square = i*i
        sumOfSquares += square
    squaredSum = sumOfFirstNNumbers*sumOfFirstNNumbers
    differenceOfSquares = squaredSum - sumOfSquares
    return differenceOfSquares

if __name__ == '__main__':
    print(sumSquareDifference(100))
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))