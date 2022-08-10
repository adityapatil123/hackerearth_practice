def get_indices_with_value_as_one(number: int):
    binary_string = str(bin(number)[2:])
    string_len = len(binary_string)
    indices = []
    for index, binary in enumerate(binary_string):
        if binary == "1":
            indices.append(string_len-index-1)
    return indices


def get_duplicate_friend_ids_across_plans(plans):
    all_friend_ids = []
    for p in plans:
        all_friend_ids.extend(get_indices_with_value_as_one(p))
    duplicate_friend_ids = []
    arr_size = len(all_friend_ids)
    for i in range(arr_size):
        x = all_friend_ids[i] % arr_size
        all_friend_ids[x] = all_friend_ids[x] + arr_size

    for i in range(arr_size):
        if all_friend_ids[i] >= arr_size * 2:
            duplicate_friend_ids.append(i)
    return duplicate_friend_ids


def get_max_cost_with_at_most_one_plan_removal(plan_values: list):
    max_value = 0
    duplicate_friend_ids = get_duplicate_friend_ids_across_plans(plan_values)

    for p in plan_values:
        current_plan_friend_ids = get_indices_with_value_as_one(p)
        if current_plan_friend_ids[0] in duplicate_friend_ids and p > max_value:
            max_value = p
    return max_value


t = int(input())
input_list = []
for ct in range(t):
    n = int(input())
    plan_string = input()
    plan_list = list(map(lambda p: int(p), plan_string.split(" ")))
    input_list.append((n, plan_list))

for inp in input_list:
    n = inp[0]
    plan_list = inp[1]
    print(get_max_cost_with_at_most_one_plan_removal(plan_list))
