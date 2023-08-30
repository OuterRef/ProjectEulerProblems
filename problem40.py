# <p>An irrational decimal fraction is created by concatenating the positive integers:
# $$0.12345678910{\color{red}\mathbf 1}112131415161718192021\cdots$$</p>
# <p>It can be seen that the $12$<sup>th</sup> digit of the fractional part is $1$.</p>
# <p>If $d_n$ represents the $n$<sup>th</sup> digit of the fractional part, find the value of the following expression.
# $$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$$</p>

from functools import reduce

def get_number(n):
    last_remain = remain = n
    digit_len = 0
    while remain > 0:
        last_remain = remain
        remain = remain - 9 * pow(10, digit_len) * (digit_len+1)
        digit_len += 1
    if digit_len == 1: return last_remain
    else: return int(str(pow(10, digit_len-1) + (last_remain-1) // digit_len)[last_remain % digit_len - 1])

print(reduce(lambda x, y: x * y, [get_number(i) for i in [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]]))
