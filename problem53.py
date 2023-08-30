# <p>There are exactly ten ways of selecting three from five, 12345:</p>
# <p class="center">123, 124, 125, 134, 135, 145, 234, 235, 245, and 345</p>
# <p>In combinatorics, we use the notation, $\displaystyle \binom 5 3 = 10$.</p>
# <p>In general, $\displaystyle \binom n r = \dfrac{n!}{r!(n-r)!}$, where $r \le n$, $n! = n \times (n-1) \times ... \times 3 \times 2 \times 1$, and $0! = 1$.
# </p>
# <p>It is not until $n = 23$, that a value exceeds one-million: $\displaystyle \binom {23} {10} = 1144066$.</p>
# <p>How many, not necessarily distinct, values of $\displaystyle \binom n r$ for $1 \le n \le 100$, are greater than one-million?</p>

from math import factorial

# alternative solution: yanghui triangle
def C(n , r):
    assert n >= r
    return factorial(n) / (factorial(r) * factorial(n - r))

MAX_LIM = 1_000_000

tot_sum = 0
values = set()
for n in range(23, 101):
    n_count = 0
    for r in reversed(range(1, n // 2 + 1)):
        if C(n, r) > MAX_LIM:
            values.add(C(n, r))
            n_count += 1
        else: break
    if n % 2 != 0:
        tot_sum = tot_sum + 2 * n_count
    else:
        if n_count != 0:
            tot_sum = tot_sum + 2 * (n_count - 1) + 1
        
print(tot_sum)

