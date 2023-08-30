# <p>Euler discovered the remarkable quadratic formula:</p>
# <p class="center">$n^2 + n + 41$</p>
# <p>It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.</p>
# <p>The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.</p>
# <p>Considering quadratics of the form:</p>
# <blockquote>
# $n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$<br><br><div>where $|n|$ is the modulus/absolute value of $n$<br>e.g. $|11| = 11$ and $|-4| = 4$</div>
# </blockquote>
# <p>Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.</p>

from math import sqrt

def prime(num):
    if num < 2: return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_streak(a, b):
    result = b
    n = 0
    while prime(result):
        n += 1
        result = n * n + a * n + b
    return n


prime_list = []
# sieve
marked = [False, False] + [True] * 2000 # [0, 2001]
value = 2
while value < 2001:
    if marked[value]:
        i = value
        while i < 2002:  # 所有value的倍数都排除
            marked[i] = False
            i += value
        marked[value] = True
    value += 1

for idx in range(len(marked)):
    if marked[idx]:
        prime_list.append(idx)

max_len = 0
result_ab = (0,0)
for b in prime_list:
    if b > 1000:
        break
    for ab1 in prime_list:
        a = ab1 - 1 - b
        if not abs(a) in prime_list or abs(a) >= 1000:
            continue
        else:
            streak = get_streak(a, b)
            if streak > max_len:
                max_len = streak
                result_ab = (a, b)

print(result_ab)
print(max_len)
# print(result_ab[0] * result_ab[1])
