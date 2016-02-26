from math import sqrt

def isTriplet(a,b,c):
    if a<b and b<c:
        if a*a+b*b==c*c:
            return True
        else:
            return False
    else:
        return False

triplets=[]
c=1

for a in range(1,1000):
    for b in range(a+1,1000):
        if a+2*b>1000:
            break

        c=int(sqrt(a*a+b*b))
        if isTriplet(a,b,c):
            triplets.append([a,b,c])

for triplet in triplets:
    if sum(triplet)==1000:
        print triplet[0]*triplet[1]*triplet[2]
