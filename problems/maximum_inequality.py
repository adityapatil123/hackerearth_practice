def get_binary_string_max_inequality(binary_string, str_len):
    s1 = ""
    s2 = ""
    s = [*binary_string]
    for i in range(str_len):
        s1_last = s1[-1] if len(s1) > 0 else None
        s2_last = s2[-1] if len(s2) > 0 else None
        if s1_last != s[i]:
            s1 += s[i]
        elif s2_last != s[i]:
            s2 += s[i]
        else:
            s1 += s[i]

    return find_inequality_from_string(s1) + find_inequality_from_string(s2)


def find_inequality_from_string(optimised_string):
    if len(optimised_string) == 0:
        return 0
    count = 0
    prev = optimised_string[0]
    for c in optimised_string:
        if prev != c:
            count += 1
        prev = c
    return count


t = int(input())
input_list = []
for _ in range(t):
    x_len = int(input())
    x = input()
    input_list.append((x, x_len))

for x in input_list:
    print(get_binary_string_max_inequality(x[0], x[1]))
