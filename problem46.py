# <p>It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.</p>
# \begin{align}
# 9 = 7 + 2 \times 1^2\\
# 15 = 7 + 2 \times 2^2\\
# 21 = 3 + 2 \times 3^2\\
# 25 = 7 + 2 \times 3^2\\
# 27 = 19 + 2 \times 2^2\\
# 33 = 31 + 2 \times 1^2
# \end{align}
# <p>It turns out that the conjecture was false.</p>
# <p>What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?</p>

from math import sqrt
import time

start = time.time()
MAX_LIM = 1_000_000

prime_list = [False, False] + [True] * (MAX_LIM - 1)
# Sieve
value = 2
while value < int(sqrt(MAX_LIM + 1)) + 1:
    if prime_list[value]:
        i = value * value
        while i < MAX_LIM + 1:
            prime_list[i] = False
            i += value
    value += 1

tgt = 9
while True:
    if prime_list[tgt] == False:
        flag = False
        for i in range(tgt):
            if prime_list[i]:
                t = sqrt((tgt - i) / 2)
                if int(t) == t:
                    flag = True
                    break
        if not flag:
            print(tgt)
            break
    tgt += 2
end = time.time()
print(end - start)
