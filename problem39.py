# <p>If $p$ is the perimeter of a right angle triangle with integral length sides, $\{a, b, c\}$, there are exactly three solutions for $p = 120$.</p>
# <p>$\{20,48,52\}$, $\{24,45,51\}$, $\{30,40,50\}$</p>
# <p>For which value of $p \le 1000$, is the number of solutions maximised?</p>

import time

start = time.time()
max_count = 0
max_p = 1
max_set = []
for p in range(1, 1001):
    p_count = 0
    p_set = []
    for c in range(1, p-1):
        ab = (p*p-2*p*c)/2
        if 0 < ab < c*c and ab == int(ab):
            for a in range(1, c):
                b = ab / a
                if b == int(b) and a*a + b*b == c*c:
                    p_count += 1
                    p_set.append([a, b, c])
    if p_count > max_count:
        max_count  = p_count
        max_p = p
        max_set = p_set
end = time.time()

print(max_p)
print(max_count)
print(max_set)
print(end-start)
