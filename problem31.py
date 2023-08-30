# <p>In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:</p>
# <blockquote>1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).</blockquote>
# <p>It is possible to make £2 in the following way:</p>
# <blockquote>1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p</blockquote>
# <p>How many different ways can £2 be made using any number of coins?</p>

def get_ways(remain, max_value_idx, values_list):
    count = 0
    max_value_count = 0
    if max_value_idx == 0:
        return 1
    while True:
        new_remain = remain - (max_value_count * values_list[max_value_idx])
        if new_remain < 0:
            break
        else:
            count += get_ways(new_remain, max_value_idx - 1, values_list)
        max_value_count += 1
    return count

values_list = [1, 2, 5, 10, 20, 50, 100, 200]
print(get_ways(200, len(values_list)-1, values_list))
