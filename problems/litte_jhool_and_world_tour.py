# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/litte-jhool-and-world-tour-1/

def get_free_country_status_dict(country_len):
    country_status = {}
    for i in range(country_len):
        country_status[i] = False
    return country_status


def get_country_range_list_dict(country_len):
    country_range_list = {}
    for i in range(country_len):
        country_range_list[i] = []
    return country_range_list


def get_actual_range_from_x_y_range(x_val, y_val, country_len):
    if x_val <= y_val:
        return list(range(x_val, y_val+1))
    else:
        return list(range(x_val, country_len)) + list(range(0, y_val+1))


def check_if_country_possible_in_prev_range(country, prev_range_list, country_status):
    for country_range in prev_range_list:
        if country in country_range:
            country_index = country_range.index(country)
            country_range_len = len(country_range)
            next_country_index = country_index+1
            while next_country_index < country_range_len:
                next_country = country_range[next_country_index]
                if not country_status[next_country]:
                    country_status[next_country] = True
                    return True
    return False


def check_if_world_tour_possible(country_len, ranges_len, country_ranges):
    country_status = get_free_country_status_dict(country_len)
    actual_range_list = []
    status_change_flag_list = []
    for i in range(ranges_len):
        x_val, y_val = country_ranges[i]
        status_changed_flag = False
        actual_range = get_actual_range_from_x_y_range(x_val, y_val, country_len)
        for c in actual_range:
            if country_status[c] is False:
                country_status[c] = True
                status_changed_flag = True
                break

        if not status_changed_flag:
            for c in actual_range:
                if check_if_country_possible_in_prev_range(c, actual_range_list, country_status):
                    status_changed_flag = True
                    break

        status_change_flag_list.append(status_changed_flag)
        actual_range_list.append(actual_range)

    return all(status_change_flag_list)


t = int(input())
input_list = []
for ct in range(t):
    n_m_string = input()
    n_m_splits = n_m_string.split(" ")
    n, m = int(n_m_splits[0]), int(n_m_splits[1])
    given_country_ranges = []
    for _ in range(m):
        cr_str = input()
        cr_splits = cr_str.split(" ")
        x, y = int(cr_splits[0]), int(cr_splits[1])
        given_country_ranges.append((x, y))
    input_list.append((n, m, given_country_ranges))


for n, m, given_country_ranges in input_list:
    res = "YES" if check_if_world_tour_possible(n, m, given_country_ranges) else "NO"
    print(res)


# Accepted Solution
def print_if_world_tour_possible():
    for i in range(int(input())):
        n,m=map(int,input().split())

        countries=[]
        count=0
        for i in range(m):
            x,y=map(int,input().split())
            if x == y:
                count = 1
                break

            elif x > n and x > y:
                if (x-y) > n:
                    count = 1

        if count == 0:
            print("YES")
        else:
            print("NO")
