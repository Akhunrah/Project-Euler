from common_functions import digitSum

maximum = 0

for i in range(1,100):
    for j in range(1,100):
        maximum = max(maximum,digitSum(pow(i,j)))
print maximum
