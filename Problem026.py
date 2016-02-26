from common_functions import *

def findQuotientList(number):
    quotient = 10/number
    remainder = 10%number
    quotientList=[quotient]
    for j in range(10000):
        quotient=remainder*10/number
        remainder = remainder*10%number
        quotientList.append(quotient)
    #Get rid of leading zeroes
    number=number/10
    while number!=0:
        quotientList.pop(0)
        number=number/10
    return quotientList

def findCycleLength(quotientList):

    cycleBoolean=False
    flag=True

    while cycleBoolean==False:
        
        while flag:
            number = quotientList.pop(0)
            
            try:
                cycleLength=quotientList.index(number)+1
                flag = False
                quotientList.insert(0,number)
            except ValueError:
                flag = True
            
        #print cycleLength
        cycle = []
        for i in range(cycleLength):
            number=quotientList.pop(i)
            cycle.append(number)
            quotientList.insert(i,number)

        quotientString=''
        quotientLength=cycleLength*(len(quotientList)/cycleLength)
        for num in quotientList:
            quotientString+=str(num)
            if len(quotientString)==quotientLength:
                break
            
        cycleString=''
        for num in cycle:
            cycleString+=str(num)

        #print quotientString,cycleString
            
        newString=quotientString[cycleLength:quotientLength]
        if newString.find(cycleString)==-1:
            flag = True
            quotientList.pop(0)
            continue
        elif newString.find(cycleString) !=0:
            char = newString[0]
            cycleLength+=newString[1:].index(char)+1
        else:
            return cycleLength
    
            
dataL=[]
for i in range(2,1000):
    cycleLength=findCycleLength(findQuotientList(i))
    print i,cycleLength
    dataL.append(cycleLength)

print 'The max is at i= ', 2+dataL.index(max(dataL))

#print findCycleLength(findQuotientList(102))


##print findCycleLength(findQuotientList(16))

##quotientList=findQuotientList(16)
##quotientString='00000000'
##cycleString='0625'
##print quotientString.find(cycleString)
