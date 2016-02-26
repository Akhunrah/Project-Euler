target = 3
sums = []

sumsL = []


for i in range(target+1):
    sums.append(0)

sums[0]=1

for i in range(1,target):
    for j in range(i,target+1):
        sums[j]+=sums[j-i]
    sumsL.append([i,sums[i]])

for sums in sumsL:
    print sums
 
