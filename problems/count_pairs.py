t = int(input())
input_list = []
for ct in range(t):
    n = int(input())
    x = int(input())
    y = int(input())
    a_list_string = input()
    b_list_string = input()
    a_list = list(map(lambda p: int(p), a_list_string.split(" ")))
    b_list = list(map(lambda p: int(p), b_list_string.split(" ")))
    input_list.append((n, x, y, a_list, b_list))


for inp in input_list:
    n = inp[0]
    x = inp[1]
    y = inp[2]
    a_list = inp[3]
    b_list = inp[4]
    count = 0

    lhs_count_dict = {}
    for i in range(n):
        lhs_value = ((a_list[i] & x) ^ (a_list[i] & y))
        if lhs_value in lhs_count_dict.keys():
            lhs_count_dict[lhs_value] += 1
        else:
            lhs_count_dict[lhs_value] = 1

    count = 0
    for i in range(n):
        rhs_value = ((b_list[i] & x) ^ (b_list[i] & y))
        if rhs_value in lhs_count_dict.keys():
            count += lhs_count_dict[rhs_value]

    print(count)
