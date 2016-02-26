def handValue(hand):
    numL=[]
    suitL=[]
    for card in hand:
        numL.append(card[0])
        suitL.append(card[1])

    
    value=0
    flushFlag=False
    suit=suitL[0]
    if suitL.count(suit)==5:
        flushFlag=True

    numL.sort()
    straightFlag=False
    for i in range(1,len(numL)):
        if numL[i]-numL[i-1]==1:
            straightFlag=True
            continue
        else:
            straightFlag=False
            break
        
    if straightFlag and flushFlag:
        value += 900+sum(numL)
    elif straightFlag:
        value+=400+sum(numL)
    elif flushFlag:
        value+=500 + max(numL)
    else:

        num1=numL.pop(0)
        if numL.count(num1)==3:
            value+=700 +num1
        elif numL.count(num1)==2:
            value+=300
            numL.pop(0)
            numL.pop(0)
            if numL[0]==numL[1]:
                value+=300+max(num1,numL[0])
            else:
                value+=num1
        elif numL.count(num1)==1:
            value+=100
            numL.pop(0)
            num2=numL.pop(0)
            if numL.count(num2)==2:
                value+=500+max(num1,num2)
            elif numL.count(num2)==1:
                value+=100+max(num1,num2)
            elif numL[0]==numL[1]:
                value+=100+max(num1,numL[0])
            else:
                value+=num1
        else:
            num1=numL.pop(0)
            if numL.count(num1)==3:
                value+=700+4*num1
            elif numL.count(num1)==2:
                value+=300+num1
            elif numL.count(num1)==1:
                value+=100
                numL.pop(0)
                if numL[0]==numL[1]:
                    value+=100+max(num1,numL[0])
                else:
                    value+=num1
            else:
                num1=numL.pop(0)
                if numL.count(num1)==2:
                    value+=300+num1
                elif numL.count(num1)==1:
                    value+=100+num1
                elif numL[0]==numL[1]:
                    value+=100+numL[1]
                else:
                    value+=numL[1]
    return value
                    
            
    




f=open('Problem054.dat','r')
lines=f.readlines()
f.close()

hand1L=[]
hand2L=[]

for line in lines:
    line=line[0:len(line)-1]
    cards=line.split()
    hand1=[]
    hand2=[]
    for card in cards:
        value = card[0]
        suit = card[1]
        if value=='2':
            card=[2,suit]
        elif value=='3':
            card=[3,suit]
        elif value=='4':
            card=[4,suit]
        elif value=='5':
            card=[5,suit]
        elif value=='6':
            card=[6,suit]
        elif value=='7':
            card=[7,suit]
        elif value=='8':
            card=[8,suit]
        elif value=='9':
            card=[9,suit]
        elif value == 'T':
            card=[10,suit]
        elif value=='J':
            card=[11,suit]
        elif value=='Q':
            card=[12,suit]
        elif value=='K':
            card=[13,suit]
        elif value=='A':
            card=[14,suit]
        
        if len(hand1)<5:
            hand1.append(card)
        else:
            hand2.append(card)
    hand1L.append(hand1)
    hand2L.append(hand2)

wins=0
for hand1,hand2 in zip(hand1L,hand2L):
    if handValue(hand1)>handValue(hand2):
        wins+=1
print wins
