from common_functions import *

DL=[]
xL=[]
yL=[]

for i in range(1,1001):
    if isSquare(i)==False:
        DL.append(i)

for i in range(len(DL)):
    x=0
    y=0
    D=DL[i]
    size=0
    while True:
        x,y=convergentFraction(continuedFractionSQRT(D,size))
        if x*x-D*y*y==1:
            xL.append(x)
            yL.append(y)
            break
        else:
            size+=1



xMax=max(xL)
ind=xL.index(xMax)
print DL[ind]

