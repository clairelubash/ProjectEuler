# Project Euler - Question 7

# What is the 10001st prime number?

import time

start = time.time()

def isPrime(n):
    
    for i in range(2,n):
        if n%i == 0:
            return False    
    return True


def nthPrime(n):

    primes = [2]
    x = 3

    while(len(primes) < n):
        if isPrime(x):
            primes.append(x)
        x += 2

    return primes[-1]

    
print(nthPrime(10001))
print('Time elapsed:', (time.time() - start), 'seconds')
