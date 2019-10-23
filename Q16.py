# Project Euler - Question 16

# What is the sum of the digits of the number 2^1000?

import time

def solve(n):

    exp = list(str(2**n))

    return(sum([int(i) for i in exp]))

print(solve(1000))
print('Time Elapsed:', time.perf_counter(), 'seconds')
