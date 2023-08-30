# <p>The prime $41$, can be written as the sum of six consecutive primes:</p>
# $$41 = 2 + 3 + 5 + 7 + 11 + 13.$$
# <p>This is the longest sum of consecutive primes that adds to a prime below one-hundred.</p>
# <p>The longest sum of consecutive primes below one-thousand that adds to a prime, contains $21$ terms, and is equal to $953$.</p>
# <p>Which prime, below one-million, can be written as the sum of the most consecutive primes?</p>

import time

start = time.time()
MAX_LIM = 1_000_000

check_prime = [False, False] + [True] * (MAX_LIM - 1)
prime_list = []
prime_sum = 0
# Sieve
value = 2
while value < MAX_LIM:
    if check_prime[value]:
        prime_sum += value
        if prime_sum < MAX_LIM:
            prime_list.append(value)
        i = value * value
        while i < MAX_LIM + 1:
            check_prime[i] = False
            i += value
    value += 1

length = 1
while True:
    for l in range(length + 1):
        h = length - l
        current_sum = sum(prime_list[l:len(prime_list)-h])
        if check_prime[current_sum]:
            end = time.time()
            print(current_sum)
            print(end - start)
            exit()
    length += 1
