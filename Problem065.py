def convergentFraction(fraction):
    m=fraction[0]
    sequence = fraction[1][::-1]
    p=1
    q=sequence[0]
    for i in range(1,len(sequence)):
        pNew=q
        qNew=q*sequence[i]+p
        p=pNew
        q=qNew
    return p+m*q,q

def sumOfDigits(integer):
    total=0
    while integer!=0:
        total+=integer%10
        integer=integer/10
    return total
    
    

##for i in range(0,5):
##    seq=[2 for j in range(i+1)]
##    p,q=convergentFraction([1,seq])
##    print i+1,',\t', p,',\t',q



##for i in range(0,10):
##    seq=[]
##    for j in range(0,i+1):
##        if j%3==0 or j%3==2:
##            seq.append(1)
##        else:
##            seq.append(2*(j/3+1))
##    p,q=convergentFraction([2,seq])
##    print i+1,',\t', p,',\t',q
            
seq=[]
for j in range(0,101):
    if j%3==0 or j%3==2:
        seq.append(1)
    else:
        seq.append(2*(j/3+1))
p,q=convergentFraction([2,seq])
print sumOfDigits(p)
