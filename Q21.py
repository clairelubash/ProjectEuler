# Project Euler - Question 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# Evaluate the sum of all the amicable numbers under 10000. 


import time

def d(n):
    
    return(sum(x for x in range(1, n // 2 + 1) if not (n % x)))


def ami(n):
    
    s = set()
    
    for i in range(1, n):
        a = d(i)
        b = d(a)
        
        if (i == b) and (a != b):
            s.add(a)
            
    return(sum(s))

print(ami(10000))
print('Time Elapsed:', time.perf_counter(), 'seconds')