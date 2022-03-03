import math
import time

start_time = time.perf_counter_ns()

def digitRecognition(digit, tens):
    spelling = ""
    if digit[0] == 0:
        digit = digit[1]
    elif digit == "1":
        spelling = "one"
    elif digit == "2":
        spelling = "two"
        if tens:
            spelling = "twenty"
    elif digit == "3":
        spelling = "three"
        if tens:
            spelling = "thirty"
    elif digit == "4":
        spelling = "four"
        if tens:
            spelling = "forty"
    elif digit == "5":
        spelling = "five"
        if tens:
            spelling = "fifty"
    elif digit == "6":
        spelling = "six"
        if tens:
            spelling = "sixty"
    elif digit == "7":
        spelling = "seven"
        if tens:
            spelling = "seventy"
    elif digit == "8":
        spelling = "eight"
        if tens:
            spelling = "eighty"
    elif digit == "9":
        spelling = "nine"
        if tens:
            spelling = "ninety"
    elif digit == "10":
        spelling = "ten"
    elif digit == "11":
        spelling = "eleven"
    elif digit == "12":
        spelling = "twelve"
    elif digit == "13":
        spelling = "thirteen"
    elif digit == "14":
        spelling = "fourteen"
    elif digit == "15":
        spelling = "fifteen"
    elif digit == "16":
        spelling = "sixteen"
    elif digit == "17":
        spelling = "seventeen"
    elif digit == "18":
        spelling = "eighteen"
    elif digit == "19":
        spelling = "nineteen"
    return spelling

def magnitude(scaleIn000s):
    magnitude = ""
    if scaleIn000s == 3:
        magnitude = "billion"
    elif scaleIn000s == 2:
        magnitude = "million"
    elif scaleIn000s == 1:
        magnitude = "thousand"
    return magnitude

def countingUnits(scaleIn000s, digits):
    if digits == "000":
        return magnitude(scaleIn000s)
    elif len(digits) == 3:
            if digits[1:] == "00":
                return digitRecognition(digits[0], False) + "hundred"
            else:
                return digitRecognition(digits[0], False) + "hundred" + "and" + countingUnits(scaleIn000s, digits[1:])
    elif len(digits) == 2:
        if int(digits)>19:
            return digitRecognition(digits[0], True) + countingUnits(scaleIn000s, digits[1])
        else:
            if digits[0] == "1":
                return digitRecognition(digits, False) + magnitude(scaleIn000s)
            else:
                return digitRecognition(digits[1], False) + magnitude(scaleIn000s)
    else:
        return digitRecognition(digits, False) + magnitude(scaleIn000s)

def numberToSpelling(number):
    strNumber = str(number)
    numberInThirds = []
    while len(strNumber)>0:
        if len(strNumber)-3 > 0:
            numberInThirds.append(strNumber[len(strNumber)-3:len(strNumber)])
            strNumber = strNumber[:len(strNumber)-3]
        else:
            numberInThirds.append(strNumber)
            strNumber = ""
    spelling = ""
    for i in range(len(numberInThirds)):
        spelling += countingUnits(len(numberInThirds) - i - 1, numberInThirds[len(numberInThirds) - i - 1])
    return spelling

def numberOfLetters(number):
    numberWord = numberToSpelling(number)
    return len(numberWord)

if __name__ == '__main__':
    sumOfLetters = 0
    for n in range(0,1001):
        print(numberToSpelling(n))
        print(numberOfLetters(n))
        sumOfLetters += numberOfLetters(n)
    print(sumOfLetters)
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))