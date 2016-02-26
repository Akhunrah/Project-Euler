from common_functions import primeSieve,isPrime

def isPermutation(num1,num2):

    num1Set = set(str(num1))
    num2Set = set(str(num2))
    if num1Set.issubset(num2Set) and num2Set.issubset(num1Set):
        return True
    else:
        return False


    

primes = primeSieve(10000)

for prime in primes:
    if prime+6660 >=10000:
        break
    if prime >1000 :
        if isPrime(prime+3330) and isPrime(prime+6660):
            if isPermutation(prime,prime+3330) and isPermutation(prime, prime+6660):
                print prime,prime+3330,prime+6660

