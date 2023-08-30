# <p>A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.</p>
# <p>A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.</p>

# <p>As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.</p>
# <p>Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.</p>

from math import sqrt
import time 

def d(n):
    divisors = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sum(divisors)

if __name__ == "__main__":
    start = time.time()
    abundant_nums = []
    for n in range(12, 28124):
        if d(n) > n:
            # abundant number
            abundant_nums.append(n)
    sum_abundant_nums = [False] * (28123*2+1)
    for i in range(len(abundant_nums)):
        for j in range(i, len(abundant_nums)):
            sum_abundant_nums[abundant_nums[i] + abundant_nums[j]] = True
    tot_sum = 0
    for n in range(28124):
        if not sum_abundant_nums[n]:
            tot_sum += n
    end = time.time()
    print(tot_sum)
    print(end-start)
