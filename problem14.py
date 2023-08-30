# <p>The following iterative sequence is defined for the set of positive integers:</p>
# <ul style="list-style-type:none;">
# <li>$n \to n/2$ ($n$ is even)</li>
# <li>$n \to 3n + 1$ ($n$ is odd)</li></ul>
# <p>Using the rule above and starting with $13$, we generate the following sequence:
# $$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$</p>
# <p>It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.</p>
# <p>Which starting number, under one million, produces the longest chain?</p>
# <p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>

max_len = 0
max_num = 0
for num in range(1, 1_000_000):
    chain_len = 1
    n = num
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        chain_len += 1
    if chain_len > max_len:
        max_len = chain_len
        max_num = num

print(max_len)
print(max_num)
