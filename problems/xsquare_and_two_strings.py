# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/xsquare-and-two-strings-1/


def check_if_any_substring_match(string1, string2):
    string1_len = len(string1)
    string2_len = len(string2)
    already_done = set()
    if string1_len > 0 and string2_len > 0:
        for i in range(string1_len-1):
            sub_str = string1[i:i+2]
            flag = sub_str not in already_done and sub_str in string2
            already_done.add(sub_str)
            if flag:
                return "Yes"
    return "No"


t = int(input())
input_list = []
for ct in range(t):
    str1 = input()
    str2 = input()
    input_list.append((str1, str2))


for inp in input_list:
    print(check_if_any_substring_match(inp[0], inp[1]))
