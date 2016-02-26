import numpy as np
import itertools as it

triangleNumL=[]
squareNumL=[]
pentagonNumL=[]
hexagonNumL=[]
heptagonNumL=[]
octagonNumL=[]


n=1
while True:
    triangleNum = n*(n+1)/2
    squareNum = n*n
    pentagonNum = n*(3*n-1)/2
    hexagonNum = n*(2*n-1)
    heptagonNum = n*(5*n-3)/2
    octagonNum = n*(3*n-2)
    #string = str(triangleNum)+'\t'+str(squareNum)+'\t'+str(pentagonNum)+'\t'+str(hexagonNum)+'\t'+str(heptagonNum)+'\t'+str(octagonNum)
    #print string
    
    n+=1
    
    if triangleNum>=10000:
        break
    elif triangleNum>=1000:
        triangleNumL.append(triangleNum)

    if 1000<=squareNum<=10000:
        squareNumL.append(squareNum)

    if 1000<=pentagonNum<=10000:
        pentagonNumL.append(pentagonNum)

    if 1000<=hexagonNum<=10000:
        hexagonNumL.append(hexagonNum)

    if 1000<=heptagonNum<=10000:
        heptagonNumL.append(heptagonNum)

    if 1000<=octagonNum<=10000:
        octagonNumL.append(octagonNum)


allNumLL=[octagonNumL,heptagonNumL,hexagonNumL,pentagonNumL,squareNumL,triangleNumL]
#
#
perms = list(it.permutations([1,2,3,4,5]))



for num0 in allNumLL[0]:
    
    for perm in perms:
        start=num0%100
        end=num0/100
        numL=[num0]
        for i in perm:
            length=len(numL)
            nextNumL=allNumLL[i]
            
            for nextNum in nextNumL:
                if nextNum/100==start:
                    start=nextNum%100
                    numL.append(nextNum)

            if len(numL)==len(allNumLL) and start==end:
                print perm
                print numL
                print sum(numL)
            





    
