# <p>The cube, $41063625$ ($345^3$), can be permuted to produce two other cubes: $56623104$ ($384^3$) and $66430125$ ($405^3$). In fact, $41063625$ is the smallest cube which has exactly three permutations of its digits which are also cube.</p>
# <p>Find the smallest cube for which exactly five permutations of its digits are cube.</p>

import time
from typing import Dict, List

def count_digit(num):
    cnt_list = [0]*10
    for s in str(num):
        cnt_list[int(s)] += 1
    return cnt_list

start = time.time()
cubic_dict: Dict[Dict[int, int], List[int]] = {}

for i in range(10_000):
    cubic = i**3
    cnt_list = str(count_digit(cubic))
    if cnt_list in cubic_dict:
        cubic_dict[cnt_list].append(cubic)
    else:
        cubic_dict[cnt_list] = [cubic]

for k, v in cubic_dict.items():
    if len(v) == 5:
        print(k, v)
end = time.time()
print(end - start)
