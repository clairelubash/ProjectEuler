# Project Euler - Question 14

# Which starting number, under one million, produces the longest Collatz chain?


import time

def coll(n):
    
    if n <= 0:
        return 0
    c = 1
    
    while n > 1:
        
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        c += 1
        
    return c

x = 0
ans = 0

for i in range(1000001):
    
    c = coll(i)
    
    if c > x:
        x = c
        ans = i

print(ans)
print('Time elapsed:', time.perf_counter(), 'seconds')
