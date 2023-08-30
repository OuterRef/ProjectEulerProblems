# <p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
# <p>What is the $10\,001$st prime number?</p>

from math import sqrt
import time
start = time.time()
prime_list = [2]
num = 3
while len(prime_list) < 10_001:
    is_prime = True
    for k in prime_list:
        if k > sqrt(num): 
            break
        if num % k == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(num)
    num += 2
end = time.time()
print(prime_list[-1])
print(end-start)
