# Project Euler - Question 19

# How many Sundays fell on the first of the month during the twentieth century?


import time
from datetime import date

def sunday(n):

    ans = 0

    for year in range(1901, n + 1):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:
                ans += 1

    return(ans)

print(sunday(2000))
print('Time Elapsed:', time.perf_counter(), 'seconds')
