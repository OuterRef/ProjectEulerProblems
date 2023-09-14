# <p>It is possible to show that the square root of two can be expressed as an infinite continued fraction.</p>
# <p class="center">$\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$</p>
# <p>By expanding this for the first four iterations, we get:</p>
# <p>$1 + \frac 1 2 = \frac  32 = 1.5$<br>
# $1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$<br>
# $1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$<br>
# $1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$<br></p>
# <p>The next three expansions are $\frac {99}{70}$, $\frac {239}{169}$, and $\frac {577}{408}$, but the eighth expansion, $\frac {1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.</p>
# <p>In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?</p>

from math import gcd

def simp_frac(numer, denom):
    gcd_value = gcd(numer, denom)
    if gcd_value == 1:
        return numer, denom
    else:
        return numer // gcd_value, denom // gcd_value

if __name__ == "__main__":
    count = 0
    a, b = (1, 1)
    for i in range(10_000):
        a, b = simp_frac(a + 2 * b, a + b)
        if len(str(a)) > len(str(b)):
            count += 1
    print(count)
