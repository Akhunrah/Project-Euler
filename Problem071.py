from common_functions import *
import time

def reducedFraction(numL):
    n = numL[0]
    d = numL[1]
    GCD = gcd(n,d)
    return [n/GCD,d/GCD]

finalFraction = [0,1]

dMax = 1000000
fraction=[1,1]

time0 = time.time()

for d in range(1,dMax+1):
    nMin = finalFraction[0]*d/finalFraction[1]
    nMax = 3*d/7
    for n in range(nMin,nMax+1):
        fraction = reducedFraction([n,d])
        upperBound = 3/7.0
        lowerBound = finalFraction[0]/(1.0*finalFraction[1])
        realForm = fraction[0]/(1.0*fraction[1])
        if(lowerBound < realForm and realForm < upperBound):
            finalFraction = fraction
            

print finalFraction, time.time()-time0
                
