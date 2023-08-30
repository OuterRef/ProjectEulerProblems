# <p>$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.</p>
# <p>Find the sum of all numbers which are equal to the sum of the factorial of their digits.</p>
# <p class="smaller">Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.</p>

from functools import reduce

def fact(n):
    if n == 0 or n == 1: return 1
    return reduce(lambda x, y: x * y, range(1, n+1))

tot_sum = 0
for i in range(3, 50001):
    if i == sum([fact(int(d)) for d in str(i)]):
        tot_sum += i

print(tot_sum)
