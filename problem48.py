# <p>The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.</p>
# <p>Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.</p>

import time
start = time.time()
print(str(sum(pow(i, i) for i in range(1, 1001)))[-10:])
end = time.time()
print(end - start)
