# <p>Euler's totient function, $\phi(n)$ [sometimes called the phi function], is defined as the number of positive integers not exceeding $n$ which are relatively prime to $n$. For example, as $1$, $2$, $4$, $5$, $7$, and $8$, are all less than or equal to nine and relatively prime to nine, $\phi(9)=6$.</p>
# <div class="center">
# <table class="grid center"><tr><td><b>$n$</b></td>
# <td><b>Relatively Prime</b></td>
# <td><b>$\phi(n)$</b></td>
# <td><b>$n/\phi(n)$</b></td>
# </tr><tr><td>2</td>
# <td>1</td>
# <td>1</td>
# <td>2</td>
# </tr><tr><td>3</td>
# <td>1,2</td>
# <td>2</td>
# <td>1.5</td>
# </tr><tr><td>4</td>
# <td>1,3</td>
# <td>2</td>
# <td>2</td>
# </tr><tr><td>5</td>
# <td>1,2,3,4</td>
# <td>4</td>
# <td>1.25</td>
# </tr><tr><td>6</td>
# <td>1,5</td>
# <td>2</td>
# <td>3</td>
# </tr><tr><td>7</td>
# <td>1,2,3,4,5,6</td>
# <td>6</td>
# <td>1.1666...</td>
# </tr><tr><td>8</td>
# <td>1,3,5,7</td>
# <td>4</td>
# <td>2</td>
# </tr><tr><td>9</td>
# <td>1,2,4,5,7,8</td>
# <td>6</td>
# <td>1.5</td>
# </tr><tr><td>10</td>
# <td>1,3,7,9</td>
# <td>4</td>
# <td>2.5</td>
# </tr></table></div>
# <p>It can be seen that $n = 6$ produces a maximum $n/\phi(n)$ for $n\leq 10$.</p>
# <p>Find the value of $n\leq 1\,000\,000$ for which $n/\phi(n)$ is a maximum.</p>

from math import sqrt

MAX_LIM = 1_000_001
# MAX_LIM = 11

def factorization(num):
    if num < 2: return []
    ret = []
    loop = True
    while loop:
        loop = False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                ret.append(i)
                num = num // i
                loop = True
                break
        if not loop and num != 1:
            ret.append(num)
    return ret

if __name__ == "__main__":
    div_counter = [0] * MAX_LIM

    for n in range(2, MAX_LIM):
        for i in set(factorization(n)):
            for x in range(n // i, 1 + (MAX_LIM - 1) // i):
                if i*x > n:
                    div_counter[i*x] += 1
    max_val = 0
    max_n = 0
    for n, c in enumerate(div_counter):
        if n < 2: continue
        phi = n - c - 1
        val = n / phi
        if val > max_val:
            max_val = val
            max_n = n
    print(max_n)
