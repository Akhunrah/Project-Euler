import itertools

perms = itertools.permutations('0123456789')

i=1
for perm in perms:
    if i==1000000:
        print perm
        break
    else:
        i+=1

