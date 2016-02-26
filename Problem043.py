import itertools

def fitsPattern(perm):
    divisors = [2,3,5,7,11,13,17]
    for i in range(1,8):
        numString = ''.join([perm[i],perm[i+1],perm[i+2]])
        number = int(numString)
        divisor = divisors[i-1]
        
        if number%divisor !=0:
            return False
    return True
        


digits = ['0','1','2','3','4','5','6','7','8','9']

#print list(itertools.permutations(digits))

numSum = 0

for perm in list(itertools.permutations(digits)):
    
    if fitsPattern(perm):
        print int(''.join(perm))
        numSum+= int(''.join(perm))

print numSum

