# <p>Using <a href="resources/documents/0022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.</p>
# <p>For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the $938$th name in the list. So, COLIN would obtain a score of $938 \times 53 = 49714$.</p>
# <p>What is the total of all the name scores in the file?</p>

with open("./files/problem22_file.txt", "r") as f:
    file_txt = f.readline()

names = [name[1:-1] for name in file_txt.split(",")]
names.sort()

tot_sum = 0
for idx in range(len(names)):
    tot_sum += sum([ord(l) - ord('A') + 1 for l in names[idx]]) * (idx + 1)

print(tot_sum)
