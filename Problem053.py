from common_functions import combinatorial

number=0

for n in range(22,101):
    for r in range(n):
        if combinatorial(n,r)>1000000:
            number+=1
            print number
