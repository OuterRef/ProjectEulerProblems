# <p>The $5$-digit number, $16807=7^5$, is also a fifth power. Similarly, the $9$-digit number, $134217728=8^9$, is a ninth power.</p>
# <p>How many $n$-digit positive integers exist which are also an $n$th power?</p>

tot_cnt = 0
for n in range(1, 1000):
    for i in range(1, 10):
        if len(str(pow(i, n))) == n:
            tot_cnt += 1

print(tot_cnt)
