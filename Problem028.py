# The pattern with this problem is we begin with one, then for the nth
# arm of the spiral we add 2n to the last number four times to get the next
# four diagonal numbers, ie., for n=1, the first arm we get 1,3,5,7,9.
# Followed by n=2 with 13, 17, 21, 25. The maximum number of arms is the
# dimension of the square matrix divided by 2, rounded down.

dimension = 1001
arms = range(1,(dimension+1)/2)
diagonal1 = [0]
diagonal2 = [1]
number = 1

for arm in arms:

    number+= 2*arm
    diagonal1.append(number)
    number+= 2*arm
    diagonal2.append(number)
    number+= 2*arm
    diagonal1.append(number)
    number+= 2*arm
    diagonal2.append(number)

print sum(diagonal1) + sum(diagonal2)
