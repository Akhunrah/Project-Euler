import time
from common_functions import primeSieve

def isPrime(prime,primes):
    for divisor in primes:
        if prime == divisor:
            break
        elif prime%divisor == 0:
            return False
        else:
            continue
    return True

maximum = 1000000
n = 20
time0 = time.time()
primes = primeSieve(maximum)
print max(primes)
time1 = time.time()
print time1-time0


while True:
    time2 = time.time()
    n+=1
    if sum(primes[1:n+1])>max(primes):
        break
    for i in range(len(primes)-n):
        number = sum(primes[i:i+n])
        if number>max(primes):
            break
        if isPrime(number,primes):
            thePrime= number
            nmax = n
    time3 = time.time()
    print n, thePrime, nmax, time3-time2

print thePrime
    
