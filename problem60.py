# <p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
# <p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p>

from math import sqrt

MAX_LIM = 10_000

class Solver():
    def __init__(self):
        self.check_prime = [False, False] + [True] * (MAX_LIM - 1)
        self.prime_list = []
        self.pair_list_dict = {}
        self._sieve()
        self._getPairs()

    def _sieve(self):
        value = 2
        while value < MAX_LIM + 1:
            if self.check_prime[value]:
                self.prime_list.append(value)
                i = value * value
                while i < MAX_LIM + 1:
                    self.check_prime[i] = False
                    i += value
            value += 1
    
    def _getPairs(self):
        l = len(self.prime_list)
        for ia in range(l):
            self.pair_list_dict[self.prime_list[ia]] = []
            for ib in range(ia + 1, l):
                if self.concatAsPrime(self.prime_list[ia], self.prime_list[ib]):
                    self.pair_list_dict[self.prime_list[ia]].append(self.prime_list[ib])
                    
    def concatAsPrime(self, n, m):
        if m == n: return False
        # if int(str(n) + str(m)) > MAX_LIM:
        if not(self.largeNumIsPrime(int(str(n) + str(m))) and self.largeNumIsPrime(int(str(m) + str(n)))):
            return False
        # else:
        #     if not(self.check_prime[int(str(n) + str(m))] and self.check_prime[int(str(m) + str(n))]):
        #         return False
        return True

    @staticmethod
    def largeNumIsPrime(num):
        if num < 2: return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def inter(l1, l2):
        if l1 == [] or l2 == []: return []
        ret = []
        for i in l1:
            if i in l2:
                ret.append(i)
        return ret

    def solve(self):
        # min_sum = 1e10
        # l = len(self.candidate_primes)
        # for ia in range(l - 4):
        #     print(ia)
        #     prime_group = [self.candidate_primes[ia]]
        #     for ib in range(ia + 1, l - 3):
        #         # check a, b
        #         if self.concatAsPrime(self.candidate_primes[ib], prime_group):
        #             prime_group.append(self.candidate_primes[ib])
        #             for ic in range(ib + 1, l - 2):
        #                 # check a, b, c
        #                 if self.concatAsPrime(self.candidate_primes[ic], prime_group):
        #                     prime_group.append(self.candidate_primes[ic])
        #                     for id in range(ic + 1, l - 1):
        #                         # check a, b, c, d
        #                         if self.concatAsPrime(self.candidate_primes[id], prime_group):
        #                             prime_group.append(self.candidate_primes[id])
        #                             for ie in range(id + 1, l):
        #                                 # check a, b, c, d, e
        #                                 if self.concatAsPrime(self.candidate_primes[ie], prime_group):
        #                                     prime_group.append(self.candidate_primes[ie])
        #                                     print(prime_group)
        #                                     lowest_sum = sum(prime_group)
        #                                     if lowest_sum < min_sum:
        #                                         min_sum = lowest_sum
        #                             prime_group.pop()
        #                     prime_group.pop()
        #             prime_group.pop()
        #     prime_group.pop()
        # return min_sum
        l = len(self.prime_list)
        for ia in range(l - 1):
            for ib in range(ia + 1, l):
                self.f(self.inter(self.pair_list_dict[self.prime_list[ia]], self.pair_list_dict[self.prime_list[ib]]), 0, [self.prime_list[ia], self.prime_list[ib]])

    def f(self, list, depth=0, gather=[]):
        if depth == 2 and list != []: print(gather + list)
        while list != []:
            first = list.pop(0)
            self.f(self.inter(self.pair_list_dict[first], list), depth + 1, gather + [first])

if __name__ == "__main__":
    import time
    start = time.time()
    solver = Solver()
    end = time.time()
    print(solver.solve())
    print(end - start)
    # [13, 5197, 5701, 6733, 8389]
