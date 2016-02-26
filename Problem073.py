from common_functions import *
import time

time0 = time.time()

fractionSet = set()
fraction = []
dMax = 12000

for d in range(4,dMax+1):
    for n in range(d/3+1,(d-1)/2+1):
        fractionSet.add(tuple(reducedFraction([n,d])))

print len(fractionSet)

print time.time()-time0
