# <p>The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.</p>
# <p>There are thirteen such primes below $100$: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.</p>
# <p>How many circular primes are there below one million?</p>

import time
from math import sqrt

prime_list = [False, False] + [True] * 999_999

def rotate(num):
    sd = str(num)
    if len(sd) == 1: return True
    for x in ['0', '2', '4', '5', '6', '8']:
        if x in sd: return False
    for _ in range(len(sd)-1):
        sd = sd[1:] + sd[0]
        if not prime_list[int(sd)]: return False
    return True

if __name__ == "__main__":
    start = time.time()
    # sieve
    value = 2
    while value < int(sqrt(1_000_001)) + 1:
        if prime_list[value]:
            i = value * value
            while i < 1_000_001:
                prime_list[i] = False
                i += value
        value += 1

    count = 0
    for idx, item in enumerate(prime_list):
        if item and rotate(idx):
            count += 1
    end = time.time()

    print(count)
    print(end - start)
