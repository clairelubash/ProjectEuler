# Project Euler - Question 1

# Find the sum of all the multiples of 3 or 5 below 1000.

import time

start = time.time()

n = 1000
ans = 0

for i in range(0,n):
    if (i%3 == 0) | (i%5 == 0):
        ans += i

print(ans)
print('Time elapsed:', (time.time() - start), 'seconds')

