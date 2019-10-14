# Project Euler - Question 10

# Find the sum of all the primes below two million.

import time

start = time.time()


def primes(n):

    ''' implementation of the Sieve of Eratosthenes method which returns a
        list of all primes less than an input '''

    sieve = [True] * n
    
    for i in range(3, int(n**0.5) + 1, 2):
        
        if sieve[i]:
            sieve[i*i :: 2*i] = [False] * ((n - i*i - 1) // (2*i) + 1)
            
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


print(sum(primes(200000)))
print('Time elapsed:', (time.time() - start), 'seconds')
