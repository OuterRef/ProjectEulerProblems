# <p>Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.</p>
# <div class="center">
# <img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
# <p>How many such routes are there through a $20 \times 20$ grid?</p>

import time

# 边长41时的杨辉三角正中间的值
def yanghui(l, inv=False):
    ret = [] if inv else [1]
    assert len(l) >= 2
    for i in range(len(l)-1):
        ret.append(l[i] + l[i+1])
    if not inv:
        ret.append(1)
    return ret

start = time.time()
l = [1, 1]
while len(l) != 21:
    l = yanghui(l)
while len(l) != 1:
    l = yanghui(l, inv=True)
end = time.time()
print(l[0])
print(end-start)
