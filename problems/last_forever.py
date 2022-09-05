# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/special-sum-3/


def check_if_string_is_palindrome(start_index, end_index):
    return substring_palindromic_flag_list[start_index][end_index]


def get_number_of_palindromic_strings(s, i, s_len):
    number_of_palindromic_strings = 0
    start = i
    if start+s_len-1 < total_str_len:
        for end in range(start+s_len-1, total_str_len):
            if end < start:
                number_of_palindromic_strings += 1
            elif check_if_string_is_palindrome(start, end):
                number_of_palindromic_strings += 1
        return number_of_palindromic_strings
    else:
        return 0


def check_for_palindrome_substring():
    for i in range(total_str_len):
        start_index, end_index = i, i
        find_palindrome_flag_recursive(start_index, end_index)
        if i != total_str_len - 1:
            start_index, end_index = i, i+1
            find_palindrome_flag_recursive(start_index, end_index)


def find_palindrome_flag_recursive(start_index, end_index):
    if input_str[start_index] == input_str[end_index]:
        substring_palindromic_flag_list[start_index][end_index] = True
        if start_index != 0 and end_index != total_str_len-1:
            start_index -= 1
            end_index += 1
            find_palindrome_flag_recursive(start_index, end_index)


input_str = input()
t = int(input())
i_len_list = []
for ct in range(t):
    i_len_string = input()
    splits = i_len_string.split(" ")
    i_value = int(splits[0])
    len_value = int(splits[1])
    i_len_list.append((i_value, len_value))

total_str_len = len(input_str)
substring_palindromic_flag_list = [[False for x in range(total_str_len)] for y in range(total_str_len)]
check_for_palindrome_substring()

for i_value, len_value in i_len_list:
    print(get_number_of_palindromic_strings(input_str, i_value, len_value))

# print(check_if_string_is_palindrome("abaaba"))
