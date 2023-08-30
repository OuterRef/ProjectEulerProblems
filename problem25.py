# <p>The Fibonacci sequence is defined by the recurrence relation:</p>
# <blockquote>$F_n = F_{n - 1} + F_{n - 2}$, where $F_1 = 1$ and $F_2 = 1$.</blockquote>
# <p>Hence the first $12$ terms will be:</p>
# \begin{align}
# F_1 &amp;= 1\\
# F_2 &amp;= 1\\
# F_3 &amp;= 2\\
# F_4 &amp;= 3\\
# F_5 &amp;= 5\\
# F_6 &amp;= 8\\
# F_7 &amp;= 13\\
# F_8 &amp;= 21\\
# F_9 &amp;= 34\\
# F_{10} &amp;= 55\\
# F_{11} &amp;= 89\\
# F_{12} &amp;= 144
# \end{align}
# <p>The $12$th term, $F_{12}$, is the first term to contain three digits.</p>
# <p>What is the index of the first term in the Fibonacci sequence to contain $1000$ digits?</p>

fnum_list = [1, 1]

while len(str(fnum_list[-1])) < 1000:
    fnum_list.append(fnum_list[-1] + fnum_list[-2])

print(len(fnum_list))

## Fibonacci terms converge to (n)*Phi=(n+1), where Phi is the Golden Ratio (1+sqrt5)/2.
## But 1e999 is too large for float, so we use log
from math import sqrt, log10
phi = (1 + sqrt(5)) / 2.0
n = 1
while(n * log10(phi) < 999):
    n += 1
print(n+1)
