# <p>All square roots are periodic when written as continued fractions and can be written in the form:</p>

# $\displaystyle \quad \quad \sqrt{N}=a_0+\frac 1 {a_1+\frac 1 {a_2+ \frac 1 {a3+ \dots}}}$

# <p>For example, let us consider $\sqrt{23}:$</p>
# $\quad \quad \sqrt{23}=4+\sqrt{23}-4=4+\frac 1 {\frac 1 {\sqrt{23}-4}}=4+\frac 1  {1+\frac{\sqrt{23}-3}7}$

# <p>If we continue we would get the following expansion:</p>

# $\displaystyle \quad \quad \sqrt{23}=4+\frac 1 {1+\frac 1 {3+ \frac 1 {1+\frac 1 {8+ \dots}}}}$

# <p>The process can be summarised as follows:</p>
# <p>
# $\quad \quad a_0=4, \frac 1 {\sqrt{23}-4}=\frac {\sqrt{23}+4} 7=1+\frac {\sqrt{23}-3} 7$<br>
# $\quad \quad a_1=1, \frac 7 {\sqrt{23}-3}=\frac {7(\sqrt{23}+3)} {14}=3+\frac {\sqrt{23}-3} 2$<br>
# $\quad \quad a_2=3, \frac 2 {\sqrt{23}-3}=\frac {2(\sqrt{23}+3)} {14}=1+\frac {\sqrt{23}-4} 7$<br>
# $\quad \quad a_3=1, \frac 7 {\sqrt{23}-4}=\frac {7(\sqrt{23}+4)} 7=8+\sqrt{23}-4$<br>
# $\quad \quad a_4=8, \frac 1 {\sqrt{23}-4}=\frac {\sqrt{23}+4} 7=1+\frac {\sqrt{23}-3} 7$<br>
# $\quad \quad a_5=1, \frac 7 {\sqrt{23}-3}=\frac {7 (\sqrt{23}+3)} {14}=3+\frac {\sqrt{23}-3} 2$<br>

# $\quad \quad a_6=3, \frac 2 {\sqrt{23}-3}=\frac {2(\sqrt{23}+3)} {14}=1+\frac {\sqrt{23}-4} 7$<br>
# $\quad \quad a_7=1, \frac 7 {\sqrt{23}-4}=\frac {7(\sqrt{23}+4)} {7}=8+\sqrt{23}-4$<br>
# </p>

# <p>It can be seen that the sequence is repeating. For conciseness, we use the notation $\sqrt{23}=[4;(1,3,1,8)]$, to indicate that the block (1,3,1,8) repeats indefinitely.</p>

# <p>The first ten continued fraction representations of (irrational) square roots are:</p>
# <p>
# $\quad \quad \sqrt{2}=[1;(2)]$, period=$1$<br>
# $\quad \quad \sqrt{3}=[1;(1,2)]$, period=$2$<br>
# $\quad \quad \sqrt{5}=[2;(4)]$, period=$1$<br>
# $\quad \quad \sqrt{6}=[2;(2,4)]$, period=$2$<br>
# $\quad \quad \sqrt{7}=[2;(1,1,1,4)]$, period=$4$<br>
# $\quad \quad \sqrt{8}=[2;(1,4)]$, period=$2$<br>
# $\quad \quad \sqrt{10}=[3;(6)]$, period=$1$<br>
# $\quad \quad \sqrt{11}=[3;(3,6)]$, period=$2$<br>
# $\quad \quad \sqrt{12}=[3;(2,6)]$, period=$2$<br>
# $\quad \quad \sqrt{13}=[3;(1,1,1,1,6)]$, period=$5$
# </p>
# <p>Exactly four continued fractions, for $N \le 13$, have an odd period.</p>
# <p>How many continued fractions for $N \le 10\,000$ have an odd period?</p>

import time
from math import sqrt

class FracItem:
    def __init__(self, add, n, sub, denom, prev=None):
        self.add = add
        self.n = n
        self.sub = sub
        self.denom = denom
        self.prev: FracItem = prev
        assert self.add   > 0, f"add: {self.add} <= 0"
        assert self.n     > 0, f"n: {self.n} <= 0"
        assert self.sub   > 0, f"sub: {self.sub} <= 0"
        assert self.denom > 0, f"denom: {self.denom} <= 0"
    
    def valid(self):
        return getFloorSqrt(self.n) >= self.sub
    
    def getNextFracItem(self):
        assert (self.n - self.sub**2) % self.denom == 0, self.__repr__()
        new_n = self.n
        new_denom = (self.n - self.sub**2) // self.denom
        new_add = self.sub // new_denom + 1
        new_sub = - (self.sub - new_add * new_denom)
        return FracItem(new_add, new_n, new_sub, new_denom, self)
    
    def addOffset(self):
        self.add += 1
        self.sub += self.denom
        return self

    def __repr__(self):
        return f"{self.add} + (sqrt({self.n}) - {self.sub}) / {self.denom}"


def getFloorSqrt(n):
    return int(sqrt(n))

def solve(f: FracItem):
    history = []
    while True:
        if f.__repr__() in history:
            start = history.index(f.__repr__())
            loop = len(history) - start
            break
        if f.valid():
            # print(f)
            history.append(f.__repr__())
            f = f.getNextFracItem()
        else:
            f = f.prev.addOffset()
            # print("addOffset:", f)
            history.pop()

    # print(history)
    return loop

if __name__ == "__main__":
    start = time.time()
    count = 0
    for n in range(2, 10_001):
        floor_sqrt = getFloorSqrt(n)
        if sqrt(n) == floor_sqrt: continue
        f = FracItem(floor_sqrt, n, floor_sqrt, 1)
        if solve(f) % 2 != 0:
            count += 1
    end = time.time()
    print(count)
    print(end - start)
