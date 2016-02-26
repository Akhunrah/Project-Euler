f=open('Problem013.dat','r')
lines = f.readlines()

nums=[]
for line in lines:
    nums.append(int(line))

for num in nums:
    print num

print sum(nums)
