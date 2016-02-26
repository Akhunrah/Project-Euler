def isSunday(day):
    #Sundays are defined to be the 1st day of the week, Saturdays the 0th day.
    if day%7==1:
        return True
    else:
        return False

def isLeapYear(year):
    if year%4==0:
        if year%400==0:
            return True
        elif year%100!=0:
            return True
        else:
            return False
    else:
        return False
def numOfDaysInMonth(month,year):

    set31 = [1,3,5,7,8,10,12]
    set30 = [4,6,9,11]
    if month in set31:
        return 31
    if month in set30:
        return 30
    else:
        if isLeapYear(year):
            return 29
        else:
            return 28


#First of January 1900 is a Monday, thus day is 2, year is 1900

day = 2
year1 = 1900

# Advance 365 days and find modulo 7 for Jan 1,1990
day = (day+365)%7
year1 +=1


years = range(year1,2001)
counter = 0

for year in years:
    for month in range(1,13):
        day+=numOfDaysInMonth(month,year)
        if isSunday(day):
            counter+=1

print counter


