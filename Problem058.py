from common_functions import isPrime3
import time

startTime=time.time()

arm = 1
number = 1
primes = [2]
numOfPrimes = 0
numOfNonPrimes = 1
ratio = 1


while ratio>0.1:
    for i in range(4):
        number+=2*arm
##        while max(primes)<number:
##            primes = includeNextPrime(primes)
        if isPrime3(number):
            numOfPrimes +=1
        else:
            numOfNonPrimes+=1
            
    ratio = numOfPrimes/(1.0*(numOfPrimes+numOfNonPrimes))
    print arm,ratio
    
        
        
    arm+=1

print 2*arm-1, time.time()-startTime

