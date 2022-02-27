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
    print(sum)
