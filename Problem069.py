from common_functions import *
##
###Really, really long way
##ratioL=[-1,-1]
##for n in range(2,1000001):
##    denom=totient(n)
##    ratio=(1.0*n)/denom
##    print '\t',n,'\t',denom,'\t',ratio
##    ratioL.append(ratio)
##
##print ratioL.index(max(ratioL))


primes=primeSieve(200)
    
maxValue=1000000
number=1

for prime in primes:
    number=number*prime
    if number>maxValue:
        itMax=primes.index(prime)
        break

number=1
for i in range(itMax):
    number=number*primes[i]
print number
