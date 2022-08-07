# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
input_lines = """4
2
5
7
9
4
2 9 2
7 2 3
7 9 7
9 5 1
7
9"""

inputs = [x for x in input_lines.splitlines()]
n = int(inputs[0])
member_ids = inputs[1: (n + 1)]
e = int(inputs[n + 1])
edge_strings = inputs[(n + 2): (n + e + 2)]
a = int(inputs[n + e + 2])
b = int(inputs[n + e + 3])
edges = []
for e in edge_strings:
    splits = e.split(" ")
    edges.append((int(splits[0]), int(splits[1]), int(splits[2])))

print(edges)


def find_min_message_time(follower):
    followings_without_b = list(filter(lambda x: x[0] == follower and x[1] != b, edges))
    followings_with_b = list(filter(lambda x: x[0] == follower and x[1] == b, edges))

    message_times2 = [f[2] + find_min_message_time(f[1]) for f in followings_without_b]

    if len(followings_with_b) > 0:
        message_time = followings_with_b[0][2]
        message_times2.append(message_time)

    min_following_time = min(message_times2) if len(message_times2) > 0 else float("inf")
    return min_following_time


def find_with_a_in_path(following):
    followers_without_a = list(filter(lambda x: x[1] == following and x[0] != a, edges))
    followers_with_a = list(filter(lambda x: x[1] == following and x[0] == a, edges))
    follower_ids = [f[0] for f in followers_with_a]
    for f in followers_without_a:
        follower_ids.append(f[0]) if find_with_a_in_path_recursive(f[0]) else None

    return follower_ids


def find_with_a_in_path_recursive(following):
    followers_with_a = list(filter(lambda x: x[1] == following and x[0] == a, edges))
    if len(followers_with_a) > 0:
        return True

    followers_without_a = list(filter(lambda x: x[1] == following and x[0] != a, edges))
    find_flags = [find_with_a_in_path_recursive(f[0]) for f in followers_without_a]
    return any(find_flags)


print(find_min_message_time(a))
print(find_with_a_in_path(b))


