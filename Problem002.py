import time

startTime=time.time()
total=0
fib0=0
fib1=1
fibnew =fib0+fib1

while(fibnew<4000000):
    fib0=fib1
    fib1=fibnew
    fibnew = fib0+fib1

    #print fibnew

    if(fibnew%2==0):
        total+=fibnew


print total,time.time()-startTime

