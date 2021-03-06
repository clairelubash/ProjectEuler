# Project Euler - Question 29

# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

import time

def dist_pow(n):

    ans = set()
    
    for x in range(2, n+1):
        for y in range(2, n+1):
            ans.add(x**y)

    return(len(ans))

print(dist_pow(100))
print('Time Elapsed:', time.perf_counter(), 'seconds')
