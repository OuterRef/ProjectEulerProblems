# <p>The first two consecutive numbers to have two distinct prime factors are:</p>
# \begin{align}
# 14 &amp;= 2 \times 7\\
# 15 &amp;= 3 \times 5.
# \end{align}
# <p>The first three consecutive numbers to have three distinct prime factors are:</p>
# \begin{align}
# 644 &amp;= 2^2 \times 7 \times 23\\
# 645 &amp;= 3 \times 5 \times 43\\
# 646 &amp;= 2 \times 17 \times 19.
# \end{align}
# <p>Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?</p>

# from math import sqrt

# def divisors(num):
#     div = set()
#     while num > 1:
#         for i in range(2, num + 1):
#             if num % i == 0:
#                 div.add(i)
#                 num = num // i
#                 break
#     return div

# for num in range(644, 1_000_000):
#     if len(divisors(num)) == 4 and len(divisors(num+1)) == 4 and len(divisors(num+2)) == 4 and len(divisors(num+3)) == 4:
#         print(num)
#         break


Limit = 1000000     # Search under 1 million for now
factors = [0] * Limit # number of prime factors.
count = 0
for i in range(2, Limit):
    if factors[i] == 0:
        # i is prime
        count = 0
        val = i
        while val < Limit:
            factors[val] += 1
            val += i
    elif factors[i] == 4:
        count += 1
        if count == 4:
            print(i - 3)  # First number
            break
    else:
        count = 0
