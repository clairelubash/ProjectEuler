# Project Euler - Question 22

# Using names.txt, sort it by alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?


import time

with open('names.txt') as f:
    x = f.read()

x = x.strip().replace('"', '').split(',')
x.sort()


def score(name):

    return(sum([ord(x) - 64 for x in list(name)]))


ans = 0

for i in range(len(x)):
    ans += score(x[i])*(i+1)

print(ans)
print('Time Elapsed:', time.perf_counter(), 'seconds')