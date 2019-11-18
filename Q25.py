# Project Euler - Question 25

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import time

def fib(n):

    a, b = 1, 1
    index = 1

    while len(str(a)) < n:
        index += 1
        a, b = b, a + b

    return(index)

print(fib(1000))
print('Time Elapsed:', time.perf_counter(), 'seconds')
