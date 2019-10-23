# Project Euler - Question 12

# What is the value of the first triangle number to have over 500 divisors?

import time
from functools import reduce
import math

def calc_factors(n):
    
    return set(reduce(list.__add__, ([i, n//i]
                                     for i in range(1, int(math.sqrt(n)) + 1)
                                     if n%i ==0)))
        
def solve(n):

    ans = 0
    
    for i in range(1, n+1):
        ans = ans + i
        if len(calc_factors(ans)) > 500:
            break

    if len(calc_factors(ans)) <= 500:
        print('Enter a higher value for n.')
    else:
        print('Triangle number:', ans, '\nNumber of Divisors:', len(calc_factors(ans)))

    
solve(20000)
print('Time Elapsed:', time.perf_counter(), 'seconds')
