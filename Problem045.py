from math import sqrt

def isPentagonalNumber(number):

    n = int((1 + sqrt(1-4*3*(-2*number)))/(6.0))

    if number == n*(3*n-1)/2:
        return True
    else:
        return False

    
def isHexagonalNumber(number):
    n = int((1 + sqrt(1+8*number))/(4.0))

    if number == n*(2*n-1):
        return True
    else:
        return False


n = 285

while True:
    n+=1
    triNum = n*(n+1)/2

    if isPentagonalNumber(triNum) and isHexagonalNumber(triNum):
        print triNum
        break
    
