# Project Euler - Question 15

# How many routes are there to the bottotm right corner through a 20x20 grid?


import time
from math import factorial

def cbc(n):

    return(factorial(2*n)/(factorial(n)**2))

print(int(cbc(20)))
print('Time Elapsed:', time.perf_counter(), 'seconds')
