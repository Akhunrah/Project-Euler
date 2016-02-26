def isPalindrome(number):
    number1=number
    number2=0
    while number!=0:
        number2=10*number2+number%10
        number=number/10
    if number1==number2:
        return True
    else:
        return False

default = 999

palindromes = []

for i in range(900,1000):
    for j in range(900,1000):
        number = i*j
        if isPalindrome(number):
            palindromes.append(number)

largest=0
for palindrome in palindromes:
    if palindrome>largest:
        largest = palindrome
print largest
