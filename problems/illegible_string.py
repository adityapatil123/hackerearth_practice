# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/illegible-string/


def is_char_v_or_w(c):
    return c in ["v", "w"]


def is_char_v(c):
    return c == "v"


def get_min_and_max_of_v_w_substring(v_count, w_count):
    max_count = 2*w_count + v_count
    min_count = max_count // 2 + max_count % 2
    return min_count, max_count


def get_min_and_max_len_of_string(str_len, string):
    min_count, max_count = 0, 0
    v_count, w_count = 0, 0
    for i in range(str_len):
        if is_char_v_or_w(string[i]):
            if is_char_v(string[i]):
                v_count += 1
            else:
                w_count += 1

            if i == str_len - 1 or not is_char_v_or_w(string[i+1]):
                min_count_s, max_count_s = get_min_and_max_of_v_w_substring(v_count, w_count)
                min_count += min_count_s
                max_count += max_count_s
                v_count, w_count = 0, 0
        else:
            min_count += 1
            max_count += 1
    return min_count, max_count


n = int(input())
s = input()


min_len, max_len = get_min_and_max_len_of_string(n, s)
print(f"{min_len} {max_len}")
