# Project Euler - Question 17

# If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?

import time
from num2words import num2words

def num_to_word(n):

    ans = 0

    for i in range(1, n+1):
        x = num2words(i).replace(' ', '').replace('-', '')
        ans += len(x)

    return(ans)

print(num_to_word(1000))
print('Time Elapsed:', time.perf_counter(), 'seconds')

