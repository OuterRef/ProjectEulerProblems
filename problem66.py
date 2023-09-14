# <p>Consider quadratic Diophantine equations of the form:
# $$x^2 - Dy^2 = 1$$</p>
# <p>For example, when $D=13$, the minimal solution in $x$ is $649^2 - 13 \times 180^2 = 1$.</p>
# <p>It can be assumed that there are no solutions in positive integers when $D$ is square.</p>
# <p>By finding minimal solutions in $x$ for $D = \{2, 3, 5, 6, 7\}$, we obtain the following:</p>
# \begin{align}
# 3^2 - 2 \times 2^2 &amp;= 1\\
# 2^2 - 3 \times 1^2 &amp;= 1\\
# {\color{red}{\mathbf 9}}^2 - 5 \times 4^2 &amp;= 1\\
# 5^2 - 6 \times 2^2 &amp;= 1\\
# 8^2 - 7 \times 3^2 &amp;= 1
# \end{align}
# <p>Hence, by considering minimal solutions in $x$ for $D \le 7$, the largest $x$ is obtained when $D=5$.</p>
# <p>Find the value of $D \le 1000$ in minimal solutions of $x$ for which the largest value of $x$ is obtained.</p>

# Reference: https://blog.csdn.net/wh2124335/article/details/8871535

from math import sqrt
from typing import List
from problem64 import FracItem, getFloorSqrt, solve
from problem57 import simp_frac

def genFracFromSeq(seq: List[int]):
    numer = 1
    denom = 0
    for n in reversed(seq):
        numer, denom = denom, numer
        numer += (denom * n)
    return numer, denom


if __name__ == "__main__":
    max_x = 0
    result = 0
    for d in range(2, 1001):
        if int(sqrt(d)) == sqrt(d): continue
        loop = solve(FracItem(getFloorSqrt(d), d, getFloorSqrt(d), 1))
        assert loop[-1] == 2 * loop[0]
        loop_len = len(loop) - 1
        p, q = simp_frac(*genFracFromSeq(loop[:-1]))
        if loop_len % 2 == 0:
            x, y = p, q
        else:
            x, y = 2 * p**2 + 1, 2 * p * q
        if x > max_x:
            max_x = x
            result = d
    print(result)
