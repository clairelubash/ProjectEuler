# Project Euler - Question 3

# What is the largest prime factor of the number 600851475143 ?

import time

start = time.time()

def maxPrimeFact(n):
 
    ans = 1
 
    while n % 2 == 0:
        ans = 2
        n = n/2
 
    x = 3
    while n != 1:
        while (n % x == 0 and n != 1):
            ans = x
            n = n/x
        x += 2
 
    return ans

print(maxPrimeFact(600851475143))
print('Time elapsed:', (time.time() - start), 'seconds')
