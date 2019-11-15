# Project Euler - Question 28

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time

n = 1001; ans = 1; val = 1

for i in range(1, int((n + 1)/2)):
    val = val + i + 2
    ans += val

print(ans)
print('Time Elapsed:', time.perf_counter(), 'seconds')