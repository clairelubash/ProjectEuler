# Project Euler - Question 24

# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


import time
from itertools import permutations

p = permutations([0,1,2,3,4,5,6,7,8,9])

for count, item in enumerate(p):
    
    if count == 999999:
        
        ans = ''.join(str(i) for i in item)
        print(ans)

print('Time Elapsed:', time.perf_counter(), 'seconds')