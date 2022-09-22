# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/perfect-subarray-43560f46/

import math


def get_perfect_squares(arr):
    max_sum = sum(arr)
    perfect_squares = []
    current_val = 1
    while current_val*current_val <= max_sum:
        perfect_squares.append(current_val*current_val)
        current_val += 1
    return perfect_squares


def check_if_perfect_square_without_math_fn(num, perfect_squares):
    return num in perfect_squares


def check_if_perfect_square(num):
    r = math.sqrt(num)
    return r - math.floor(r) == 0


def get_sub_array_count_with_perfect_square(arr_len, main_array):
    count = 0
    for i in range(arr_len):
        i_sum = 0
        for j in range(i, arr_len):
            i_sum += main_array[j]
            if check_if_perfect_square(i_sum):
                count += 1
    return count


n = int(input())
a_str_splits = input().split(" ")
a = [int(x) for x in a_str_splits]
print(get_sub_array_count_with_perfect_square(n, a))
