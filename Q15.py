# Project Euler - Question 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, how many routes are there to the bottotm right corner through a 20x20 grid?

import time
from math import factorial

n = 20
ans = factorial(2*n)/(factorial(n)**2)

print(int(ans))
print('Time Elapsed:', time.perf_counter(), 'seconds')