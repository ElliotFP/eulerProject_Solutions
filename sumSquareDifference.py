def sumSquareDifference(firstNNumbers):
    sumOfFirstNNumbers = 0
    sumOfSquares = 0
    for i in range(firstNNumbers+1):
        sumOfFirstNNumbers += i
        square = i*i
        sumOfSquares += square
    squaredSum = sumOfFirstNNumbers*sumOfFirstNNumbers
    differenceOfSquares = squaredSum - sumOfSquares
    print(differenceOfSquares)
    return differenceOfSquares
