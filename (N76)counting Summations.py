import math
import time

start_time = time.time()

def CountWays(n):
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(1, n):

        for j in range(i, n + 1):
            table[j] += table[j - i]

    return table[n]

def summationCount(number):
    count = 0
    count = sumRecursive(number, count)
    print(count)
    return count

def sumRecursive(n, count):
    if n == 1:
        count+=1
        print(count)
        return
    else:
        if n%2==0:
            count += sumRecursive(n//2, count)
            count += sumRecursive(n//2, count)
        else:
            count += sumRecursive(n//2, count)
            count += sumRecursive(n//2 + 1, count)

if __name__ == '__main__':
    print("time elapsed: {:.2f}s".format(time.time() - start_time))