# <p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once; for example, the $5$-digit number, $15234$, is $1$ through $5$ pandigital.</p>
# <p>The product $7254$ is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is $1$ through $9$ pandigital.</p>
# <p>Find the sum of all products whose multiplicand/multiplier/product identity can be written as a $1$ through $9$ pandigital.</p>
# <div class="note">HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</div>

import time

def pandigital(a, b, p):
    digit_list = [False] * 10
    tot_str = str(a) + str(b) + str(p)
    if len(tot_str) != 9 or '0' in tot_str:
        return False
    else:
        for s in tot_str:
            if not digit_list[int(s)]:
                digit_list[int(s)] = True
            else:
                return False
    return sum(digit_list[1:]) == 9

start = time.time()
products = set()
# 1 x 4 -> 4
for a in range(1, 10):
    for b in range(1000, 10_000):
        p = a * b
        if pandigital(a, b, p):
            products.add(p)
# or 2 x 3 -> 4
for a in range(10, 100):
    for b in range(100, 1000):
        p = a * b
        if pandigital(a, b, p):
            products.add(p)
end = time.time()

print(sum(products))
print(end-start)
