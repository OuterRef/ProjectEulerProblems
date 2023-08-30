# <p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.</p>
# <p>What is the largest $n$-digit pandigital prime that exists?</p>

from math import sqrt

def prime(num):
    if num < 2: return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def pandigital(num):
    digit_list = [False] * 8
    s_num = str(num)
    for x in ['0', '8', '9']:
        if x in s_num: return False
    else:
        for s in s_num:
            if not digit_list[int(s)]:
                digit_list[int(s)] = True
            else:
                return False
    return sum(digit_list[1:]) == 7

max_num = 0
for num in range(1234567, 7654322):
    if num > max_num and pandigital(num) and prime(num):
        max_num = num
    
print(max_num)
