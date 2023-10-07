# <p>By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.</p>
# <p class="monospace center"><span class="red"><b>3</b></span><br><span class="red"><b>7</b></span> 4<br>
# 2 <span class="red"><b>4</b></span> 6<br>
# 8 5 <span class="red"><b>9</b></span> 3</p>
# <p>That is, 3 + 7 + 4 + 9 = 23.</p>
# <p>Find the maximum total from top to bottom in <a href="resources/documents/0067_triangle.txt">triangle.txt</a> (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.</p>
# <p class="smaller"><b>NOTE:</b> This is a much more difficult version of <a href="problem=18">Problem 18</a>. It is not possible to try every route to solve this problem, as there are 2<sup>99</sup> altogether! If you could check one trillion (10<sup>12</sup>) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)</p>


# This is exactly the same as problem18
with open("./files/problem67_file.txt", "r") as f:
    NUM_STR = f.read()

digit_list = [[int(num) for num in line.split()] for line in NUM_STR.split('\n')]

for layer_idx in reversed(range(1, len(digit_list))):
    # print(layer_idx)
    for n in range(len(digit_list[layer_idx])-1):
        digit_list[layer_idx-1][n] += max(digit_list[layer_idx][n], digit_list[layer_idx][n+1])
print(digit_list[0][0])
