def sumOfMultiplesOf3or5LowerThan(number):
    sum = 0
    for x in range(number):
    #loop through the numbers lower than and add if divisible by 3 or 5
        if x%3==0 or x%5==0:
            sum += x
    print(sum)