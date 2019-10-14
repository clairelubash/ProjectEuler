# Project Euler - Question 4

# Find the largest palindrome made from the product of two 3-digit numbers.

import time

start = time.time()

n = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        p = i*j
        if p > n:
            if str(p) == str(p)[::-1]:
                n = p

print(n)
print('Time elapsed:', (time.time() - start), 'seconds')
