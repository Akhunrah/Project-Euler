from common_functions import isPrime2,primeSieve
from math import sqrt

number = 9

maximum = 10000
primes = primeSieve(maximum)

flag = True



while number<=maximum and flag:
    number+=2
    if isPrime2(number,primes):
        continue
    else:
        for i in range(1, int(sqrt(number))):
            if isPrime2(number - 2*pow(i,2),primes):
                flag = True
                break
            flag = False
print number
        
