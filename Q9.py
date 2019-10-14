# Project Euler - Question 9

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import time

start = time.time()

for a in range(1, 500):
    for b in range(1, 500):
        
        c = 1000 - a - b
        
        if a < b < c:
            if a**2 + b**2 == c**2:
                
                print(a*b*c)

print('Time elapsed:', (time.time() - start), 'seconds')
