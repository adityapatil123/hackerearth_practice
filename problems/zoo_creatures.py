def get_hcf(x: int, y: int):
    if x == 0:
        return y
    elif x > y:
        greater_no, smaller_no = x, y
        return get_hcf(greater_no % smaller_no, smaller_no)
    else:
        greater_no, smaller_no = y, x
        return get_hcf(greater_no % smaller_no, smaller_no)


def get_lcm(x: int, y: int, hcf: int):
    return (x*y)//hcf


def get_no_of_hands_for_creature(no_of_creatures: int, lcm_of_creatures: int):
    return lcm_of_creatures // no_of_creatures


t = int(input())
n_m_string_list = []
for ct in range(t):
    n_m_string = input()
    n_m_string_list.append(n_m_string)

for s in n_m_string_list:
    splits = s.split(" ")
    n_value = int(splits[0])
    m_value = int(splits[1])
    hcf = get_hcf(n_value, m_value)
    lcm = get_lcm(n_value, m_value, hcf)
    print(f"{get_no_of_hands_for_creature(n_value, lcm)} {get_no_of_hands_for_creature(m_value, lcm)}")
