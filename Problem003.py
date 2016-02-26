import math
import time


def isPrime(number):
    divisor=2
    while divisor <=math.sqrt(number):
        if number%divisor == 0:
            return False
        else:
            divisor+=1
    return True
    

startTime = time.time()
number = 600851475143
divisor = 2

while number!=1:
    if isPrime(divisor):
        
        if number%divisor==0:
            number = number/divisor
            print divisor
        else:
            divisor+=1
    else:
        divisor+=1

print time.time()-startTime
