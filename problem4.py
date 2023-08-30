# <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
# <p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

import time

def is_palindromic(num):
    str_num = str(num)
    len = str_num.__len__()
    for i in range(len // 2):
        if str_num[i] != str_num[-i-1]:
            return False
    return True

start = time.time()
max_padlin = 0
for a in reversed(range(100, 1000)):
    if max_padlin//a > a:
        break
    for b in reversed(range(max(100, max_padlin//a), a)):
        if is_palindromic(a*b):
            max_padlin = a*b
end = time.time()

print(max_padlin)
print(end-start)
