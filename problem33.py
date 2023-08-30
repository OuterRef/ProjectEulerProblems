# <p>The fraction $49/98$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $49/98 = 4/8$, which is correct, is obtained by cancelling the $9$s.</p>
# <p>We shall consider fractions like, $30/50 = 3/5$, to be trivial examples.</p>
# <p>There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.</p>
# <p>If the product of these four fractions is given in its lowest common terms, find the value of the denominator.</p>

def curious(num, denom):
    orig_v = 1.0 * num / denom
    if num % 10 == 0 and denom % 10 == 0: return False
    s_num = str(num)
    s_denom = str(denom)
    pair = ()
    for i in range(2):
        for j in range(2):
            if s_num[i] == s_denom[j]:
                pair = (i, j)
                break
    if pair == (): return False
    new_num = int(s_num[(pair[0] + 1) % 2])
    new_denom = int(s_denom[(pair[1] + 1) % 2])
    if new_denom == 0: return False
    return orig_v == new_num / new_denom

ans = []
for i in range(10, 100):
    for j in range(i+1, 100):
        # i / j
        if curious(i, j):
            ans.append([i, j])
print(ans)
