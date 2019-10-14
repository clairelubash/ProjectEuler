# Project Euler - Question 5

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

import math, time

start = time.time()

n = 20
ans = 1

for i in range(1,n):
    ans *= i // math.gcd(i, ans)

print(ans)
print('Time elapsed:', (time.time() - start), 'seconds')
