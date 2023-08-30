# <p>If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.</p>
# <p>If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used? </p>
# <br><p class="note"><b>NOTE:</b> Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance with British usage.</p>

dec_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten_to_nineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tys = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
other = ["hundred", "thousand", "and"]

sum = 0
for w in dec_words:
    sum += len(w)
dec_len = sum
for w in ten_to_nineteen:
    sum += len(w)
for ty in tys:
    sum += len(ty)*10
    sum += dec_len
one_to_ninety_nine = sum

for w in dec_words:
    sum += len(w) + len(other[0])
    sum += (len(w) + len(other[0]) + len(other[2]))*99
    sum += one_to_ninety_nine
sum += len("one") + len(other[1])
print(sum)
