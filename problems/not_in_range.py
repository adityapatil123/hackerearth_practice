# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/not-in-range-44d19403/

def get_actual_ranges_by_removal_of_overlapping(ranges):
    ranges.sort(key=lambda x: x[0])
    actual_ranges = []
    for interval in ranges:
        if not actual_ranges or actual_ranges[-1][1] < interval[0]:
            actual_ranges.append(interval)
        else:
            actual_ranges[-1][1] = max(actual_ranges[-1][1], interval[1])
    return actual_ranges


def find_sum_of_missing_numbers(ranges):
    s = 10**6 * (10**6 + 1) // 2
    actual_ranges = get_actual_ranges_by_removal_of_overlapping(ranges)

    for i in actual_ranges:
        a, b = i[0] - 1, i[1]
        a_to_b_sum = (b - a) * (b + a + 1) // 2
        s -= a_to_b_sum
    return s


n = int(input())
ranges_here = []
for _ in range(n):
    r = input()
    r_splits = r.split(" ")
    first = int(r_splits[0])
    last = int(r_splits[1])
    ranges_here.append([first, last])

print(find_sum_of_missing_numbers(ranges_here))
