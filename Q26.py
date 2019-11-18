# Project Euler - Question 26

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
# denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


import time

def cycle(n, d):

    for i in range(1, d):
        if pow(10, i, d) == 1:
            return(i)

    return(0)

longest = max(cycle(1, x) for x in range(1, 1001, 2) if x % 5 != 0)
ans = [j for j in range(2, 1001) if cycle(1, j) == longest][0]

print(ans)
print('Time Elapsed:', time.perf_counter(), 'seconds')
