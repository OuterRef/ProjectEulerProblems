# <p>Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).<br>
# If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.</p>
# <p>For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.</p>
# <p>Evaluate the sum of all the amicable numbers under $10000$.</p>

from math import sqrt

def d(n):
    if n <= 1: return None
    divisors = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sum(divisors)

tot_sum = 0
for i in range(1, 10000):
    a = d(i)
    if a is not None:
        b = d(a)
        if i == b and i != a:
            tot_sum += i
            print(i)

print(tot_sum)
