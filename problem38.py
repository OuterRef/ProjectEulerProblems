# <p>Take the number $192$ and multiply it by each of $1$, $2$, and $3$:</p>
# \begin{align}
# 192 \times 1 &amp;= 192\\
# 192 \times 2 &amp;= 384\\
# 192 \times 3 &amp;= 576
# \end{align}
# <p>By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1,2,3)$.</p>
# <p>The same can be achieved by starting with $9$ and multiplying by $1$, $2$, $3$, $4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$.</p>
# <p>What is the largest $1$ to $9$ pandigital $9$-digit number that can be formed as the concatenated product of an integer with $(1,2, \dots, n)$ where $n \gt 1$?</p>

# n < 10
import time

def pandigital(k, n):
    # concat(k * (1, 2, ..., n))
    s = ""
    for i in range(1, n + 1):
        s += str(k * i)
    if len(s) != 9: return False, int(s)
    digits = [0] * 10
    for i in s:
        if digits[int(i)] == 0:
            digits[int(i)] = 1
        else:
            return False, int(s)
    return sum(digits[1:]) == 9, int(s)

if __name__ == "__main__":
    start = time.time()
    max_num = 0
    # d = 1, 1 + (2) + (2) + (2) + (2)
    for k in range(1, 10):
        for n in range(5, 10):
            flag, num = pandigital(k, n)
            if flag and num > max_num:
                max_num = num
    # d = 2, 2 + 2 + 2 + 3
    for k in range(25, 34):
        n = 4
        flag, num = pandigital(k, n)
        if flag and num > max_num:
            max_num = num
    # d = 3, 3 + 3 + 3
    for k in range(100, 334):
        n = 3
        flag, num = pandigital(k, n)
        if flag and num > max_num:
            max_num = num
    # d = 4, 4 + 5
    for k in range(5000, 10_000):
        n = 2
        flag, num = pandigital(k, n)
        if flag and num > max_num:
            max_num = num

    end = time.time()
    print(max_num)
    print(end-start)
