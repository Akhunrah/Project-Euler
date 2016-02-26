def returnOrderedDigits(number):
    numString=str(number)
    digitsL=[]
    for a in numString:
        digitsL.append(int(a))
    digitsL.sort()
    return digitsL

number=0
flag=True

while flag:
    number+=1
    print number
    digits=returnOrderedDigits(number)
    for i in range(2,7):
        testDigits=returnOrderedDigits(number*i)
        if(testDigits==digits):
            flag=False
        else:
            flag=True
            break

print number,number*2,number*3,number*4,number*5,number*6


            


