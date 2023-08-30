# <p>$n!$ means $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$.</p>
# <p>For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,<br>and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.</p>
# <p>Find the sum of the digits in the number $100!$.</p>

from functools import reduce
print(sum([int(n) for n in str(reduce(lambda x, y: x * y, range(1, 101)))]))
