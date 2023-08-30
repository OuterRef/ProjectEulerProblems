# <p>A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:</p>
# <p class="center">012   021   102   120   201   210</p>
# <p>What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?</p>

NUM = 999_999
LEN = 10
def fact(n):
    if n == 0: return 1
    ret = 1
    while n > 1:
        ret *= n
        n -= 1
    return ret

digit_list = [True] * LEN
remain_n = NUM
result = []
for i in reversed(range(LEN)):
    d = 0
    fact_i = fact(i)
    while (d+1) * fact_i <= remain_n:
        d += 1
    cnt = 0
    for idx, tf in enumerate(digit_list):
        if tf:
            if cnt == d:
                result.append(idx)
                digit_list[idx] = False
            cnt += 1
    remain_n -= d * fact_i
print(result)
