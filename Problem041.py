import time
from math import sqrt
from itertools import permutations
from common_functions import primeSieve, isPrime2

def is_n_pandigital(number,n):

    numString = str(number)
    
    nSet = []
    digitSet = []
    for i in range(1,n+1):
        nSet.append(str(i))
    
    digitList = list(numString)
    for digit in digitList:
        if digit in digitSet:
            continue
        else:
            digitSet.append(digit)


    if '0' in digitSet or len(numString) != len(digitSet):        
        return False
    elif nSet<=digitSet and digitSet<=nSet:        
        return True
    else:
        return False





maximum = 987654321
maxForPrimeSieve = int(sqrt(maximum))+1

time0 = time.time()
primes = primeSieve(maxForPrimeSieve)


n=9
flag = True
while n!=1 and flag:

    maxStr=''
    for i in range(n,0,-1):
        maxStr+=str(i)
    maximum = int(maxStr)
    print 'The maximum is: ' + str(maximum)

    for perm in permutations(maxStr):
        number = int(''.join(perm))        
        if isPrime2(number,primes):
            print 'The maximal pan-digital prime is: ' + str(number)
            flag = False
            break
            
    
##    n = len(str(number))
##    panBool = is_n_pandigital(number,n)
##    primeBool = isPrime2(number,primes)
##    print number, panBool,primeBool
##    if panBool and primeBool:
##        print number
##        break
        

    n-=1



time1 = time.time()
print time1-time0



