# <p>The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both bases.</p>
# <p>Find the sum of all numbers, less than one million, which are palindromic in base $10$ and base $2$.</p>
# <p class="smaller">(Please note that the palindromic number, in either base, may not include leading zeros.)</p>

def gen_bin(length):
    ans = []
    for dec in range(pow(2, length)):
        s_bin = ""
        remain = dec
        for power in reversed(range(length)):
            d = remain // pow(2, power)
            s_bin += str(d)
            remain = remain - pow(2, power) * d
        ans.append(s_bin)
    return ans
        
def bin_2_dec(b_str):
    b_len = len(b_str)
    dec = 0
    for i in range(b_len):
        dec += int(b_str[-i-1]) * pow(2, i)
    return dec

def palindromic_bin(length):
    if length == 1: return [1]
    if length == 2: return [3]
    ans = []
    if length % 2:
        for bin in gen_bin((length - 3) // 2):
            rev_bin = bin[::-1]
            ans.append(bin_2_dec('1' + bin + '0' + rev_bin + '1'))
            ans.append(bin_2_dec('1' + bin + '1' + rev_bin + '1'))
    else:
        for bin in gen_bin((length - 2) // 2):
            rev_bin = bin[::-1]
            ans.append(bin_2_dec('1' + bin + rev_bin + '1'))
    return ans

def palindromic_dec(num):
    if num % 10 == 0: return False
    return int(str(num)[::-1]) == num


if __name__ == "__main__":
    dec_list = []
    for l in range(1, 21):
        dec_list += palindromic_bin(l)
    tot_sum = 0
    for dec in dec_list:
        if dec >= 1_000_000: break
        if palindromic_dec(dec):
            tot_sum += dec
    print(tot_sum)
