n = int(input())
members = []
for _ in range(n):
    members.append(int(input()))
e = int(input())
edges = []
for _ in range(e):
    edge_string = input()
    splits = edge_string.split(" ")
    edges.append((int(splits[0]), int(splits[1])))
a = int(input())
b = int(input())

edge_mapping = {}
for edge in edges:
    if edge[1] in edge_mapping:
        edge_mapping[edge[1]].append(edge[0])
    else:
        edge_mapping[edge[1]] = [edge[0]]


def find_with_a_in_path_recursive(following, already_done=[]):
    followers_of_given_following = edge_mapping.get(following, [])
    find_flags = []

    for f in followers_of_given_following:
        if f == a:
            return True
        else:
            if f not in already_done:
                already_done.append(f)
                find_flags.append(find_with_a_in_path_recursive(f, already_done))
    return any(find_flags)


print(1 if find_with_a_in_path_recursive(b) else 0)
