# <p>The arithmetic sequence, $1487, 4817, 8147$, in which each of the terms increases by $3330$, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the $4$-digit numbers are permutations of one another.</p>
# <p>There are no arithmetic sequences made up of three $1$-, $2$-, or $3$-digit primes, exhibiting this property, but there is one other $4$-digit increasing sequence.</p>
# <p>What $12$-digit number do you form by concatenating the three terms in this sequence?</p>

from math import sqrt
import time

def prime(num):
    if num < 2: return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

start = time.time()
for tri_d in range(100, 334):
    if set(str(tri_d)) == set(str(tri_d+333)) and set(str(tri_d)) == set(str(tri_d+666)):
        for x in ['1', '3', '7', '9']:
            quad_d = tri_d * 10 + int(x)
            if prime(quad_d) and prime(quad_d + 3330) and prime(quad_d + 6660):
                print(quad_d)
                print(quad_d + 3330)
                print(quad_d + 6660)
end = time.time()
print(end - start)
