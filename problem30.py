# <p>Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# \begin{align}
# 1634 &amp;= 1^4 + 6^4 + 3^4 + 4^4\\
# 8208 &amp;= 8^4 + 2^4 + 0^4 + 8^4\\
# 9474 &amp;= 9^4 + 4^4 + 7^4 + 4^4
# \end{align}
# </p><p class="smaller">As $1 = 1^4$ is not a sum it is not included.</p>
# <p>The sum of these numbers is $1634 + 8208 + 9474 = 19316$.</p>
# <p>Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.</p>

def get_fif_pow(num):
    return sum([pow(int(n), 5) for n in str(num)])

tot_sum = 0
for i in range(2, 1_000_001):
    if get_fif_pow(i) == i:
        tot_sum += i
print(tot_sum)
