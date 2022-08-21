n = int(input())
members = []
for _ in range(n):
    members.append(int(input()))
e = int(input())
edges = []
for _ in range(e):
    edge_string = input()
    splits = edge_string.split(" ")
    edges.append((int(splits[0]), int(splits[1]), int(splits[2])))
a = int(input())
b = int(input())

edge_mapping = {}
for edge in edges:
    if edge[1] in edge_mapping:
        edge_mapping[edge[1]].append((edge[0], edge[2]))
    else:
        edge_mapping[edge[1]] = [(edge[0], edge[2])]


def find_min_message_time(following, already_done=[]):
    followers_of_given_following = edge_mapping.get(following, [])
    min_message_times = []
    for f, t in followers_of_given_following:
        if f == a:
            min_message_times.append(t)
        else:
            if f not in already_done:
                current_already_done = [f]
                current_already_done.extend(already_done)
                min_message_times.append(t + find_min_message_time(f, current_already_done))

    final_min_time = min(min_message_times) if len(min_message_times) > 0 else float("inf")
    return final_min_time


print(find_min_message_time(b))
