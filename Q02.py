# Project Euler - Question 2

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


import time

start = time.time()

n = 4000000
ans = 0

x1 = 1
x2 = 2

while x1 <= n:
    if x1%2 == 0:
        ans += x1
    x1, x2 = x2, x1 + x2

print(ans)
print('Time elapsed:', (time.time() - start), 'seconds')
