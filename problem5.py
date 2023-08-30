# <p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
# <p>What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from $1$ to $20$?</p>

# import functools
# print(functools.reduce(lambda x, y: x*y, [1, 2, 3, 2, 5, 7, 2, 3, 11, 13, 2, 17, 19]))
  

# prime_num_list   = [ 2,  3,  5,  7, 11, 13, 17, 19]
# prime_count_list = [ 1,  1,  1,  1,  1,  1,  1,  1]

# def split_num(num):
#     ret_list = [0]*len(prime_num_list)
#     if num in prime_num_list:
#         ret_list[prime_num_list.index(num)] += 1
#         return ret_list
#     for idx, k in enumerate(prime_num_list):
#         if num % k == 0:
#             ret_list[idx] += 1
#             rhs = split_num(num // k)
#             ret_list = [i + j for i, j in zip(ret_list, rhs)]
#             break
#     return ret_list

# for target in range(2, 21):
#     if target in prime_num_list:
#         continue
#     else:
#         target_count_list = split_num(target)
#         prime_count_list = [max(i, j) for i, j in zip(prime_count_list, target_count_list)]
#         print(target)
#         print(target_count_list)
#         print(prime_count_list)
#         print("-"*20)

# print(prime_count_list)
# prod = 1
# for idx in range(len(prime_num_list)):
#     prod *= pow(prime_num_list[idx], prime_count_list[idx])
# print(prod)
    
i = 1
for k in range(1, 21):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print(i)
