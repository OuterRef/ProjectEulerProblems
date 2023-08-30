# <p>A unit fraction contains $1$ in the numerator. The decimal representation of the unit fractions with denominators $2$ to $10$ are given:</p>
# \begin{align}
# 1/2 &amp;= 0.5\\
# 1/3 &amp;=0.(3)\\
# 1/4 &amp;=0.25\\
# 1/5 &amp;= 0.2\\
# 1/6 &amp;= 0.1(6)\\
# 1/7 &amp;= 0.(142857)\\
# 1/8 &amp;= 0.125\\
# 1/9 &amp;= 0.(1)\\
# 1/10 &amp;= 0.1
# \end{align}
# <p>Where $0.1(6)$ means $0.166666\cdots$, and has a $1$-digit recurring cycle. It can be seen that $1/7$ has a $6$-digit recurring cycle.</p>
# <p>Find the value of $d \lt 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.</p>

def get_loop(n):
    loop = []
    numer = 1
    pop_until = 0
    while True:
        loop.append(numer)
        d = numer // n
        if d == 0:
            numer *= 10
        else:
            numer = (numer - d * n) * 10
        if numer in loop:
            pop_until = loop.index(numer)
            break
    for _ in range(pop_until):
        loop.pop(0)
    return loop

max_len = 0
result = 0
for n in range(1, 1000):
    l = len(get_loop(n))
    if l > max_len:
        max_len = l
        result = n
print(result)
