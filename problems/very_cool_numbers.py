substring = "101"
substring_len = len(substring)


def get_coolness_count_of_number(number: int):
    number_string = str(bin(number)[2:])
    count = 0
    # for idx in range(len(number_string)):
    #     if number_string[idx: idx + substring_len] == substring:
    #         count += 1
    # return count
    x_current_string = ""
    for x in number_string:
        if x == "1":
            if x_current_string == "10":
                count += 1
            x_current_string = "1"
        else:
            if x_current_string == "1":
                x_current_string += "0"
            else:
                x_current_string = ""
    return count


def is_number_very_cool(number: int, k_value: int):
    coolness_count = get_coolness_count_of_number(number)
    return coolness_count >= k_value


def get_cool_numbers_from_range(range_max_number: int, k_value: int):
    very_cool_numbers_count = 0
    for n in range(1, range_max_number+1):
        very_cool_numbers_count = very_cool_numbers_count + 1 if is_number_very_cool(n, k_value) \
            else very_cool_numbers_count
    return very_cool_numbers_count


t = int(input())
r_k_string_list = []
for ct in range(t):
    r_k_string = input()
    r_k_string_list.append(r_k_string)

for s in r_k_string_list:
    splits = s.split(" ")
    r = int(splits[0])
    k = int(splits[1])
    print(get_cool_numbers_from_range(r, k))
