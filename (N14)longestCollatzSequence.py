import math
import time

start_time = time.time()

def collatzSequence(number):
    sequence = []
    while number != 1:
        sequence.append(number)
        if number%2==0:
            number = number//2
        else:
            number = (number*3)+1
    sequence.append(1)
    return len(sequence), sequence

def longestCollatz(underN):
    longestLength = 0
    maxN = 0
    for n in range(1, underN):
        if n%2!=0:
            length = collatzSequence(n)[0]
            if length > longestLength:
                longestLength = length
                maxN = n
    return longestLength, maxN

if __name__ == '__main__':
    print(longestCollatz(1000000))
    print("time elapsed: {:.2f}".format(time.time() - start_time))