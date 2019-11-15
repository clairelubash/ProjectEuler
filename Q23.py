# Project Euler - Question 23

# A number n is called abundant if the sum of its proper divisors exceeds n.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


import time, math
from itertools import combinations_with_replacement as combos

def div(n):
    
    ans = [1]
    
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            ans.extend([x, n//x])
            
    return((set(ans)))


def abun(n):
    
    return(sum(div(n)) > n)


def sum_not_ab():
    
    ab = (n for n in range(12, 28123) if abun(n))
    sum_ab = set(a + b for a, b in combos(ab, 2))
    not_ab = (x for x in range(28123) if x not in sum_ab)

    return(sum(not_ab))

print(sum_not_ab())
print('Time Elapsed:', time.perf_counter(), 'seconds')