def continuedFractionSQRT(x):
    m=1
    while True:
        if m*m==x:
            return [m,[]]
        elif m*m<x:
            m+=1
        else:
            m-=1
            break
    termL=[]
    #First term:
    q=x-m*m
    a=(2*m)/q
    p=a*q-m
    termL.append(a)
    for i in range(600):
        if (x-p*p)%q==0:
            qNew=(x-p*p)/q
            aNew=(m+p)/qNew
            pNew=qNew*aNew-p
            termL.append(aNew)
            a=aNew
            p=pNew
            q=qNew
            
        
    return [m,termL]

def findPeriod(intList):

    if len(intList)==0:
        return 0
    
    
    period=1
    flag=False
    while flag==False:
        seqL=[]
        i=0
        while (i+1)*period<len(intList):
            seqL.append(intList[i*period:(i+1)*period])
            i+=1
        if seqL.count(seqL[0])==len(seqL):
            return period
        period+=1
        
            
    

#print findPeriod(continuedFractionSQRT(13)[1])


number=0

for i in range(1,10000):
    frac=continuedFractionSQRT(i)
    period=findPeriod(frac[1])
##    if period >25:
##        print '%5i'%i,',','%3i'%period,',',frac
    if period%2==1:
        number+=1
print number






