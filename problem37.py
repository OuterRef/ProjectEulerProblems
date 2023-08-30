# <p>The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797$, $797$, $97$, and $7$. Similarly we can work from right to left: $3797$, $379$, $37$, and $3$.</p>
# <p>Find the sum of the only eleven primes that are both truncatable from left to right and right to left.</p>
# <p class="smaller">NOTE: $2$, $3$, $5$, and $7$ are not considered to be truncatable primes.</p>

import time
from math import sqrt

MAX_LIM = 1_000_000

prime_list = [False, False] + [True] * (MAX_LIM - 1)

def Truncatable(num):
    sd = str(num)
    if len(sd) == 1: return False
    for x in ['0', '2', '4', '5', '6', '8']:
        if x in sd: 
            if sd[0] == '2' or sd[0] == '5':
                continue
            return False
    for i in range(1, len(sd)):
        a = int(sd[i:])
        b = int(sd[:-i])
        if not (prime_list[a] and prime_list[b]): return False
    return True

if __name__ == "__main__":
    start = time.time()
    # sieve
    value = 2
    while value < int(sqrt(MAX_LIM + 1)) + 1:
        if prime_list[value]:
            i = value * value
            while i < MAX_LIM + 1:
                prime_list[i] = False
                i += value
        value += 1

    tot_sum = 0
    count = 0
    for idx, item in enumerate(prime_list):
        if item and Truncatable(idx):
            print(idx)
            count += 1
            tot_sum += idx
    end = time.time()

    print(f"sum = {tot_sum}")
    print(count)
    print(end - start)
