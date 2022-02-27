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
                    print(i*j*k)
                    return i*j*k

