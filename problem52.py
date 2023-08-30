# <p>It can be seen that the number, $125874$, and its double, $251748$, contain exactly the same digits, but in a different order.</p>
# <p>Find the smallest positive integer, $x$, such that $2x$, $3x$, $4x$, $5x$, and $6x$, contain the same digits.</p>

for x in range(1, 1_000_000):
    x_nums = set(str(x))
    ans = True
    for n in range(2, 7):
        if x_nums != set(str(n * x)):
            ans = False
            break
    if ans:
        print(x)
