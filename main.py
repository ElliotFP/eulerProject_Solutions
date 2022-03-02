import math
import time

start_time = time.time()

#Problem Number 1 : Multiples of 3 or 5

def sumOfMultiplesOf3or5LowerThan(number):
    sum = 0
    for x in range(number):
    #loop through the numbers lower than and add if divisible by 3 or 5
        if x%3==0 or x%5==0:
            sum += x
    return sum

#Problem Number 2 : Even Fibonacci Numbers

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

#Problem Number 3 : Largest Prime Factor

def assessIfPrime(number):
    if number==0 or number==1:
        return False
    else:
        for x in range(2, math.ceil(math.sqrt(number))+1):
            if x!=number and number%x==0:
                return False
        return True

def largestPrimeFactor(number):
    largestPrimeFactor = number
    for y in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % y == 0:
            divisor = number / y
            if assessIfPrime(y):
                largestPrimeFactor = y
            elif assessIfPrime(divisor):
                largestPrimeFactor = divisor
    return largestPrimeFactor

#Problem Number 4 : Largest Palindrome Product

def assessIfPalindrome(number):
    strNumber = str(number)
    similarLetterOrder = 0
    for i in range(len(strNumber)//2):
        if strNumber[i] == strNumber[len(strNumber)-i-1]:
            similarLetterOrder += 1
    if similarLetterOrder == len(strNumber)//2:
        return True
    else:
        return False

def largestPalindrome3Digits():
    high = 1000
    for i in range(1,high):
        for j in range(10):
            test = (high-i)*(high-j)
            if assessIfPalindrome(test):
                return test

#Problem Number 6 : Sum Square Difference

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

#Problem Number 7 : 10001th prime

def nthPrime(n):
    nbOfPrimes = 0
    number = 0
    while nbOfPrimes <= n:
        number += 1
        if assessIfPrime(number):
            nbOfPrimes +=1
    return number

#Problem Number 8 : Largest Product of 1000-digit Number

num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

def largestProduct(nDigitNumber, adjacent):
    number = str(nDigitNumber)
    largestProduct = 0
    for i in range(len(number)-adjacent):
        product = int(number[i])
        for j in range(1, adjacent):
            product = product*int(number[j+i])
        if largestProduct < product:
            largestProduct = product
    return largestProduct

#Problem Number 9 : Special Pythagorean Triplet

def assessIfPythagorean(a, b, c):
    if a < b and b < c and (a*a+b*b == c*c):
        return True
    else:
        return False

def specialPythagoreanTriplet():
    for i in range(335, 998):
        for j in range((1000-i)//2+1,i):
            for k in range(0, j):
                if i+j+k==1000 and assessIfPythagorean(k, j, i):
                    return i*j*k

#Problem Number 10 : Summation of Primes

def summationOfPrimes(underN):
    sum = 0
    for i in range(underN+1):
        if assessIfPrime(i):
            sum += i
    return sum

#Problem Number 11 : Largest Product in a Grid

grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
listGrid = grid.split(" ")

def largestGridProduct():
    largestProduct = 0
    for i in range(len(listGrid)):
        possibleProducts = []
        v = False
        h = False
        if i < 340:
            v = True
            possibleProducts.append(int(listGrid[i])*int(listGrid[i+20])*int(listGrid[i+40])*int(listGrid[i+60]))
        if (i-19) % 20 != 0 and (i-18) % 20 != 0 and (i-17) % 20 !=0 :
            h = True
            possibleProducts.append(int(listGrid[i])*int(listGrid[i+1])*int(listGrid[i+2])*int(listGrid[i+3]))
        if v and h:
            possibleProducts.append(int(listGrid[i]) * int(listGrid[i + 21]) * int(listGrid[i + 42]) * int(listGrid[i + 63]))
        if v and i%20!=0 and (i-1) % 20!=0 and (i-2) % 20!=0:
            possibleProducts.append(int(listGrid[i]) * int(listGrid[i + 19]) * int(listGrid[i + 38]) * int(listGrid[i + 57]))
        if possibleProducts != []:
            maxP = max(possibleProducts)
            if maxP>largestProduct:
                largestProduct = maxP
    return largestProduct

#Problem Number 12 : Highest Divisible Triangular Number

def divisors(number):
    listOfDivisors = []
    nbOfDivisors = 0
    for n in range(1, math.ceil(math.sqrt(number)) +1):
        if number%n==0:
            listOfDivisors.append(n)
            if number/n == n:
                nbOfDivisors += 1
            else:
                nbOfDivisors += 2
                listOfDivisors.append(number/n)
    return nbOfDivisors, listOfDivisors

def sumOfNaturalNumbers(n):
    sumOfNaturalNumbers = 0
    for n in range(n):
        sumOfNaturalNumbers += n
    return sumOfNaturalNumbers

def hDTN(divisibility):
    nbOfDivisors = 0
    i = 0
    while nbOfDivisors < divisibility:
        i += 1
        sum = sumOfNaturalNumbers(i)
        nbOfDivisors = divisors(sum)[0]
    return sum


#Problem Number 69 : Totient Maximum

def assessIfPrime(number):
    for x in range(math.ceil(math.sqrt(number))+1):
        if x!=0 and x!=1 and number%x==0:
            return False
        else:
            continue
    return True

def phiFunction(number):
    phi = 0
    for n in range(number):
        if gcd(n, number) == 1:
            phi += 1
    return phi

"""""""""
Shitty Non-Optimal Method with n^2

def totientMax(number):
    totientMax = 0
    totientMaxRatio = 0
    for n in range(1, number + 1):
        ratio = n / phiFunction(n)
        if totientMaxRatio < ratio:
            totientMaxRatio = ratio
            totientMax = n
    return totientMax
"""""""""

#Epic Method

def totientMax(number):
    totientMax = 1
    for n in range(1, number+1):
        if assessIfPrime(n):
            product = totientMax*n
            if product > number:
                return totientMax
            else:
                totientMax = product

#Random Method I thought I needed, but didn't. I decided to keep it, might come in handy at some point.
def primeFactors(number):
    primeFactors = []
    for n in range(1, math.ceil(math.sqrt(number))):
        if number%n == 0:
            if assessIfPrime(n):
                primeFactors.append(n)
            if assessIfPrime(number/n):
                primeFactors.append(number/n)
    return primeFactors

if __name__ == '__main__':
    print("time elapsed: {:.2f}s".format(time.time() - start_time))