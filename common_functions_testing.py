from common_functions import *
import time

number = 100000

time0 = time.time()

print totient1(number)

time1 = time.time()
print time1-time0

print totient2(number)

time2 = time.time()
print time2 -time1
