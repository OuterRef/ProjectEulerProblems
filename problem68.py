# <p>Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.</p>
# <div class="center">
# <img src="resources/images/0068_1.png?1678992052" class="dark_img" alt=""><br></div>
# <p>Working <b>clockwise</b>, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.</p>
# <p>It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.</p>
# <div class="center">
# <table width="400" cellspacing="0" cellpadding="0"><tr><td width="100"><b>Total</b></td><td width="300"><b>Solution Set</b></td>
# </tr><tr><td>9</td><td>4,2,3; 5,3,1; 6,1,2</td>
# </tr><tr><td>9</td><td>4,3,2; 6,2,1; 5,1,3</td>
# </tr><tr><td>10</td><td>2,3,5; 4,5,1; 6,1,3</td>
# </tr><tr><td>10</td><td>2,5,3; 6,3,1; 4,1,5</td>
# </tr><tr><td>11</td><td>1,4,6; 3,6,2; 5,2,4</td>
# </tr><tr><td>11</td><td>1,6,4; 5,4,2; 3,2,6</td>
# </tr><tr><td>12</td><td>1,5,6; 2,6,4; 3,4,5</td>
# </tr><tr><td>12</td><td>1,6,5; 3,5,4; 2,4,6</td>
# </tr></table></div>
# <p>By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.</p>
# <p>Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum <b>16-digit</b> string for a "magic" 5-gon ring?</p>
# <div class="center">
# <img src="resources/images/0068_2.png?1678992052" class="dark_img" alt=""><br></div>

import time
from copy import deepcopy
from typing import List


def choose(n_all, n_sel):
    def getNextItem(sel: List[bool], start: int, depth: int = 0):
        if depth == n_sel: return [sel]
        ret = []
        for i in range(start, len(sel)):
            if not sel[i]:
                new_sel = deepcopy(sel)
                new_sel[i] = True
                ret += getNextItem(new_sel, i+1, depth+1)
        return ret
    return getNextItem([False]*n_all, start=0, depth=0)

def arrange(orig):
    def putNextItem(left: List[int], result: List[int]):
        if left == []: return [result]
        ret = []
        for i in range(len(result)):
            if result[i] is None:
                new_taken = deepcopy(result)
                new_taken[i] = left[-1]
                ret += putNextItem(left[:-1], new_taken)
        return ret
    return putNextItem(orig, [None]*len(orig))

def checkValid(order: List[int], n: int):
    outers = []
    for i in range(len(order)):
        neighbor_sum = order[i % len(order)] + order[(i + 1) % len(order)]
        out = n - neighbor_sum
        if out <= 0 or out > 10:
            return False
        if out in outers or out in order:
            return False
        else:
            outers.append(out)
    return order + outers

def getString(seq: List[int]):
    inner = seq[:5]
    outer = seq[5:]
    first_idx = outer.index(min(outer))
    ret = str(seq[5 + first_idx])
    for _ in range(5):
        ret += str(inner[first_idx % 5]) + str(inner[(first_idx + 1) % 5])
        ret += str(outer[(first_idx + 1) % 5])
        first_idx += 1
    return ret[:-1]


if __name__ == "__main__":
    # print(choose(5, 3))
    # print(arrange([1,2,3]))
    start = time.time()
    all_order = []
    for sel in choose(10, 5):
        arr = [idx+1 for idx, b in enumerate(sel) if b]
        all_order += arrange(arr)[:24]
    for order in all_order:
        for n in range(20):
            result = checkValid(order, n)
            if result:
                result_str = getString(result)
                if len(result_str) == 16:
                    print(result)
                    print(result_str)
    end = time.time()
    print(end - start)
