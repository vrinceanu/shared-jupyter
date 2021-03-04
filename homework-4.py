#
# Solution for Homework 4:
# Feb 18, 2021
# Find the sum of the first 1000 prime numbers
# execute from CLI:
# python3 homework4.py
#

# primality test by brute force: try all numbers smaller than \sqrt{n}
# to see if they divide n, in other words, the reminder of the division is 0

import sys

def is_prime(n):
    for k in range(2,int(pow(n,0.5))+1):
        if n % k == 0:
            return(False)
    return(True)


n = 2
sum = 0
index = 1
Nx = int(sys.argv[1])

# search to find the first Nx prime numbers
while index <= Nx:
    if is_prime(n):
        sum += n
        index += 1
    n += 1

print(f'the sum of the first {index-1} prime numbers (up to {n}) is {sum}.')
print(f'Is this number prime? Answer: {is_prime(n)}.')