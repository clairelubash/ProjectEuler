# Project Euler - Question 27

# Find the product of the coefficients, a and b, for the quadratic expression that
# produces the maximum number of primes for consecutive values of n, starting with n = 0.

import time
import math

start = time.time()

def is_prime(k):

    '''
    checks if number is prime and returns boolean
    '''

    if k < 2:
        return(False)
    elif k == 2:
        return(True)
    elif k % 2 == 0:
        return(False)
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2):
            if k % x == 0:
                return(False)
            else:
                return(True)


def count_primes(a, b):

    '''
    returns number of consecutive primes given coefficients
    for the quadratic
    '''

    num_primes = 0

    for n in range(100):
        q = (n**2) + (a*n) + b
        if is_prime(q):
            num_primes += 1
        else:
            break

    return(num_primes)
    


def quad_coeff(a_max, b_max):

    '''
    returns products of coefficients for quadratic that produces
    max number of primes for consecutive values of n
    '''

    max_primes = 0
    max_a = 0
    max_b = 0

    for a in range(-a_max, a_max + 1):
        for b in range(-b_max, b_max + 1):
            if is_prime(b):
                if count_primes(a,b,) > max_primes:
                    max_primes = count_primes(a,b)
                    max_a = a
                    max_b = b

    return(max_a * max_b)


print(quad_coeff(1000, 1000))
print('Time elapsed:', (time.time() - start), 'seconds')
