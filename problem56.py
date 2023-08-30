# <p>A googol ($10^{100}$) is a massive number: one followed by one-hundred zeros; $100^{100}$ is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only $1$.</p>
# <p>Considering natural numbers of the form, $a^b$, where $a, b \lt 100$, what is the maximum digital sum?</p>

def digit_sum(n):
    return sum([int(s) for s in str(n)])

max_sum = 0
for a in range(90, 100):
    for b in range(90, 100):
        d_sum = digit_sum(a**b)
        if d_sum > max_sum:
            max_sum = d_sum

print(max_sum)
