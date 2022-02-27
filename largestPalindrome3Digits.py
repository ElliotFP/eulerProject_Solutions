def assessIfPalindrome(number):
    strNumber = str(number)
    similarLetterOrder = 0
    for i in range(len(strNumber)//2):
        if strNumber[i] == strNumber[len(strNumber)-i-1]:
            similarLetterOrder += 1
    if similarLetterOrder == len(strNumber)//2:
        print("True")
        return True
    else:
        print("False")
        return False

def largestPalindrome3Digits():
    high = 1000
    for i in range(1,high):
        for j in range(10):
            test = (high-i)*(high-j)
            if assessIfPalindrome(test):
                print(test)
                return test

