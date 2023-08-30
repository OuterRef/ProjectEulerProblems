# <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
# <p>What is the largest prime factor of the number $600851475143$?</p>

from math import floor, sqrt
import time

NUM = 600851475143

def split_num(num):
    is_prime = True
    max_prime = 0
    if num == 2: return 2
    for i in range(2, floor(sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            lhs_ret = split_num(i)
            rhs_ret = split_num(num / i)
            if max(lhs_ret, rhs_ret) > max_prime:
                max_prime = max(lhs_ret, rhs_ret)
    if is_prime:
        max_prime = num
    return max_prime

start = time.time()
print(split_num(NUM))
end = time.time()
print(end-start)


# start = time.time()
# primes = set([2])
# value = 3
# number = 600851475143
# while value < sqrt(number):
#     isPrime = True
#     for k in primes:
#         if value % k == 0:
#             isPrime = False
#             value += 2
#     if isPrime:
#         primes.add(value)
#         if number % value == 0:
#             number /= value
# end = time.time()
# print (number)
# print (end-start)
