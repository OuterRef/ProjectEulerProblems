# <p>By replacing the 1<sup>st</sup> digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.</p>
# <p>By replacing the 3<sup>rd</sup> and 4<sup>th</sup> digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.</p>
# <p>Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.</p>

from math import sqrt
import time

MAX_LIM = 1_000_000

class Solver():
    def __init__(self):
        self.check_prime = [False, False] + [True] * (MAX_LIM - 1)
        self._gen_prime()
        
    def _gen_prime(self):
        # Sieve
        value = 2
        while value < int(sqrt(MAX_LIM + 1)) + 1:
            if self.check_prime[value]:
                i = value * value
                while i < MAX_LIM + 1:
                    self.check_prime[i] = False
                    i += value
            value += 1

    def sub_check_prime(self, num, idx_comb, k, first):
        sub_range = [i for i in range(1, 10)]
        if not first:
            sub_range.append(0)
        s_num = str(num)
        fail_count = 0
        for sub in sub_range:
            if sub == k: continue
            lst_snum = list(s_num)
            for idx in idx_comb:
                lst_snum[idx] = str(sub)
            new_num = int(''.join(lst_snum))
            if not self.check_prime[new_num]:
                fail_count += 1
            if fail_count > len(sub_range) - 8: return False
        return True

    def solve(self):
        for prime in range(MAX_LIM + 1):
            if not self.check_prime[prime]: continue
            if prime // 1e4 == 0:
                continue
            digit_cnt_dict = self.digit_count(prime)
            for k, v in digit_cnt_dict.items():
                int_k = int(k)
                idx_combs = self.get_all_index_comb(v)
                for comb in idx_combs:
                    first = 0 in comb
                    result = self.sub_check_prime(prime, comb, int_k, first)
                    if result:
                        print(comb)
                        print(prime)
                        return 
    
    @staticmethod
    def digit_count(num):
        s_num = str(num)
        cnt = {}
        for idx in range(len(s_num)):
            if not s_num[idx] in cnt:
                cnt[s_num[idx]] = [idx]
            else:
                cnt[s_num[idx]].append(idx)
        return cnt
    
    @staticmethod
    def get_all_index_comb(idx_list):
        # a typical model of counting binary numbers
        n_idx = len(idx_list)
        all_comb = []
        for n in range(1, 2**n_idx):
            nth_comb = []
            idx = -1
            while n >= 1:
                if n % 2:
                    nth_comb.append(idx_list[idx])
                n = n // 2
                idx -= 1
            all_comb.append(nth_comb)
        return all_comb

    
if __name__ == "__main__":
    start = time.time()
    solver = Solver()
    # print(solver.digit_count(10264521))
    # print(solver.get_all_index_comb([0, 7]))
    # print(solver.sub_check_prime(56003, [2, 3], 0, False))
    solver.solve()
    end = time.time()
    print(end - start)
