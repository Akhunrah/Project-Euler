from math import sqrt

def isPentagonalNumber(number):

    n = int((1 + sqrt(1-4*3*(-2*number)))/(6.0))

    if number == n*(3*n-1)/2:
        return True
    else:
        return False
    

minimum = 10000000

n1 = 1
n2 = 2

while True:

    pent1 = n1*(3*n1-1)/2
    previousPent1 = (n1-1)*(3*(n1-1))/2
    if abs(pent1-previousPent1) > minimum:
        break
    
    while True:
        pent1 = n1*(3*n1-1)/2
        pent2 = n2*(3*n2-1)/2
        diff = abs(pent2 - pent1)
        

        if diff> minimum:
            break

        if isPentagonalNumber(pent2+pent1) and isPentagonalNumber(diff):
            print pent1,pent2,diff
            minimum = min(diff,minimum)
        n2+=1
                
    n1 += 1
    n2 = n1+1

print minimum


