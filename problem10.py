# <p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
# <p>Find the sum of all the primes below two million.</p>

# from math import sqrt
# import functools

MAX_LIM = 2_000_000

# prime_list = [2]
# num = 3
# while num < MAX_LIM:
#     is_prime = True
#     for k in prime_list:
#         if k > sqrt(num): 
#             break
#         if num % k == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_list.append(num)
#     num += 2

# print(functools.reduce(lambda x, y: x + y, prime_list))


# Sieve: 由于一个合数总是可以分解成若干个质数的乘积，那么如果把质数（最初只知道2是质数）的倍数都去掉，那么剩下的就是质数了
marked = [0] * MAX_LIM
value = 3
s = 2
while value < MAX_LIM:
    if marked[value] == 0:
        s += value
        i = value
        while i < MAX_LIM:  # 所有value的倍数都排除
            marked[i] = 1
            i += value
    value += 2
print (s)
