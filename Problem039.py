
pLargest = 1
maxSols = 0

for p in range(3,1001):
    numOfSols = 0
    for a in range(1,p):
        for b in range(1,p-a):
            c = p-a-b
            if pow(c,2)<pow(a,2)+pow(b,2):
                break
            elif pow(c,2)==pow(a,2)+pow(b,2):
                print p, a, b, c
                numOfSols+=1

    if numOfSols > maxSols:
        maxSols = numOfSols
        pLargest = p

print pLargest
