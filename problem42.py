# <p>The $n$<sup>th</sup> term of the sequence of triangle numbers is given by, $t_n = \frac12n(n+1)$; so the first ten triangle numbers are:
# $$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$</p>
# <p>By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.</p>
# <p>Using <a href="resources/documents/0042_words.txt">words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?</p>

triangle_num_list = [n*(1+n)/2 for n in range(1, 101)]
with open("./files/problem42_file.txt", "r") as f:
    line = f.readline()
words = [w[1:-1] for w in line.split(",")]
count = 0
for word in words:
    word_value = sum([ord(l)-ord('A')+1 for l in word])
    if word_value in triangle_num_list:
        count += 1
print(count)
