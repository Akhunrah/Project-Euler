def next(numer,denom):
    newDenom = numer+denom
    newNumer = numer+2*denom
    return newNumer,newDenom

n = 1
numer = 3
denom = 2
num = 0

while n != 1001:
    if len(str(numer))>len(str(denom)):
        num+=1
    numer,denom = next(numer,denom)
    n+=1

print num
    
