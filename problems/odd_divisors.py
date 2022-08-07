def square(n): return n*n


def recursive_sum(x: int):
    if x == 0:
        return 0
    elif x % 2 == 1:
        # odd
        return square((x+1)//2) + recursive_sum(x//2)
    else:
        # even
        return square(x//2) + recursive_sum(x//2)


def get_value_of_equation(n, m):
    sum_of_function_values = recursive_sum(n)
    return sum_of_function_values % m


t = int(input())
n_m_string_list = []
for ct in range(t):
    n_m_string = input()
    n_m_string_list.append(n_m_string)

for s in n_m_string_list:
    splits = s.split(" ")
    n_value = int(splits[0])
    m_value = int(splits[1])
    print(get_value_of_equation(n_value, m_value))
