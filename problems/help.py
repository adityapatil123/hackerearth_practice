# https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/help-1-0315faf6/


def get_min_number_of_fill_ups_dynamic(rem_distance, current_petrol, petrol_stations):
    if current_petrol >= rem_distance:
        return 0
    else:
        stops_required_list = []
        for i, pt in enumerate(petrol_stations):
            p_distance_from_town = pt[0]
            p_petrol_available = pt[1]
            distance_between = rem_distance - p_distance_from_town
            if current_petrol >= distance_between:
                stops_required_further = get_min_number_of_fill_ups_dynamic(p_distance_from_town,
                                                                    current_petrol+p_petrol_available-distance_between,
                                                                    petrol_stations[i+1:])
                if stops_required_further != -1:
                    stops_required_list.append(stops_required_further+1)

        print(stops_required_list)

        if len(stops_required_list) > 0:
            return min(stops_required_list)
        else:
            return -1


def get_min_number_of_fill_ups_greedy_algo(rem_distance, current_petrol, petrol_stations):
    possible_stops = sorted(petrol_stations, key=lambda x: x[0], reverse=True)
    possible_stops.append((0, 0))
    count = 0
    excess_petrol_list = []

    for st in possible_stops:
        st_distance_from_town = st[0]
        st_petrol_available = st[1]
        distance_between = rem_distance - st_distance_from_town
        current_petrol = current_petrol - distance_between
        rem_distance = st_distance_from_town

        if current_petrol >= 0:
            excess_petrol_list.append(st_petrol_available)
        else:
            while (current_petrol < 0) and (len(excess_petrol_list) > 0):
                current_petrol += excess_petrol_list.pop(excess_petrol_list.index(max(excess_petrol_list)))
                count += 1
            if current_petrol >= 0:
                excess_petrol_list.append(st_petrol_available)
            else:
                return -1
    return count


t = int(input())
petrol_stations_here = []
for _ in range(t):
    s_f = input()
    s_f_splits = s_f.split(" ")
    s = int(s_f_splits[0])
    f = int(s_f_splits[1])
    petrol_stations_here.append((s, f))
d_p = input()
d_p_splits = d_p.split(" ")
d = int(d_p_splits[0])
p = int(d_p_splits[1])
print(get_min_number_of_fill_ups_greedy_algo(d, p, petrol_stations_here))
