import math
import time

start_time = time.perf_counter_ns()

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

if __name__ == '__main__':
    print(largestPalindrome3Digits())
    print("time elapsed: {:.2f}ns".format(time.perf_counter_ns() - start_time))

