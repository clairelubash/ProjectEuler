# Project Euler - Question 20

# Find the sum of the digits in the number 100!


import time
from math import factorial

def factSum(n):

    ans = 0

    num = factorial(n)
    digits = [int(char) for char in str(num)]

    for i in digits:
        ans += i

    return(ans)


print(factSum(100))
print('Time Elapsed:', time.perf_counter(), 'seconds')
