# <p>You are given the following information, but you may prefer to do some research for yourself.</p>
# <ul><li>1 Jan 1900 was a Monday.</li>
# <li>Thirty days has September,<br />
# April, June and November.<br />
# All the rest have thirty-one,<br />
# Saving February alone,<br />
# Which has twenty-eight, rain or shine.<br />
# And on leap years, twenty-nine.</li>
# <li>A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.</li>
# </ul><p>How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?</p>

dday_dist      = [-2, 1, 1, 4, -1, 2, 4, 0, 3, -2, 1, 3]
leap_dday_dist = [-3, 0, 1, 4, -1, 2, 4, 0, 3, -2, 1, 3]

dday = 3
count = 0
for year in range(1901, 2001):
    leap_year = False
    if year % 4 == 0:
        leap_year = True
    if leap_year:
        dday = (dday + 2) % 7
        for d in leap_dday_dist:
            if (dday + d + 7) % 7 == 0:
                count += 1
    else:
        dday = (dday + 1) % 7
        for d in dday_dist:
            if (dday + d + 7) % 7 == 0:
                count += 1

print(count)
