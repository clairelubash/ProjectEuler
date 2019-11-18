# Project Euler - Question 30

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time

def fifth_pow(n):

    ans = 0
    
    for i in range(2, n+1):
        if sum([int(x)**5 for x in str(i)]) == i:
            ans += i

    return(ans)

print(fifth_pow(5*(9**5)))
print('Time Elapsed:', time.perf_counter(), 'seconds')
