from common_functions import *
import time

def reducedFraction((n,d)):
    #n = numL[0]
    #d = numL[1]
    GCD = gcd(n,d)
    return (n/GCD,d/GCD)

finalFraction = [0,1]

dMax = 8
numL = range(0,dMax+1)

time0 = time.time()

for d in range(2,dMax+1):
    if(numL[d]==d):
        for j in range(d,dMax+1):
            numL[j]=numL[j]*(d-1)/d

print sum(numL), time.time()-time0
                
