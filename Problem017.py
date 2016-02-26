def digitToString(digit):

    if digit==1:
        return "one"
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    elif digit == 9:
        return "nine"
    else:
        return ""

def maxTwoDigitNumToString(num):

    if num/10==0:
        return digitToString(num%10)
    elif num/10==1:
        if num%10 == 0:
            return "ten"
        elif num%10 == 1:
            return "eleven"
        elif num%10 == 2:
            return "twelve"
        elif num%10 == 3:
            return "thirteen"
        elif num%10 == 5:
            return "fifteen"
        elif num%10 == 8:
            return "eighteen"
        elif num%10 <=9:
            return digitToString(num%10)+"teen"
    elif num/10 == 2:
        return "twenty"+digitToString(num%10)
    elif num/10 == 3:
        return "thirty"+digitToString(num%10)
    elif num/10 == 4:
        return "forty"+digitToString(num%10)
    elif num/10 == 5:
        return "fifty"+digitToString(num%10)
    elif num/10 == 8:
        return "eighty"+digitToString(num%10)
    elif num/10<=9:
        return digitToString(num/10)+"ty"+digitToString(num%10)

def maxThreeDigitNumToString(num):

    if num/100==0:
        return maxTwoDigitNumToString(num)
    elif num%100==0:
        return digitToString(num/100)+"hundred"
    else:
        return digitToString(num/100)+"hundredand"+maxTwoDigitNumToString(num%100)
            
        

charSum=0

for i in range(1,1000):
    charSum+= len(maxThreeDigitNumToString(i))

charSum+= len("onethousand")
print charSum
    
