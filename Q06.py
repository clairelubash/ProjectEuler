# Project Euler - Question 6

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time

start = time.time()

n = 10

sum_squares = 0
square_sum = 0

for i in range(1, n+1):
    sum_squares += i**2
    square_sum += i

ans = square_sum**2 - sum_squares

print(ans)
print('Time elapsed:', (time.time() - start), 'seconds')
