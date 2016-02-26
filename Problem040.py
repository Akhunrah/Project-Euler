numString = ''
for i in range(1,185186):
    numString+=str(i)

product = 1
for power in range(0,7):
    product = product* int(numString[pow(10,power)-1])
print product
