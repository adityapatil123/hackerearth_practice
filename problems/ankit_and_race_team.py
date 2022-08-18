# https://www.hackerearth.com/problem/algorithm/ankit-and-race-team-10/?utm_source=new_practice


# def get_no_of_combinations(student_list, group_len):
#     students_len = len(student_list)
#     if group_len == 1:
#         return 1
#     elif group_len == 2:
#         return students_len*(students_len-1)//2
#     else:
#         count = 0
#         for i in range(students_len-group_len+1):
#             rem_list = student_list[i+1:]
#             count += get_no_of_combinations(rem_list, group_len=group_len-1)
#
#         return count


def get_no_of_combinations_by_formula(n, k):
    numerator = 1
    denominator = 1
    max_value = max(k, n-k)
    if max_value == n:
        return 1
    for x in range(max_value+1, n+1):
        numerator *= x
    for y in range(1, n-max_value+1):
        denominator *= y

    return numerator // denominator


t = int(input())
inputs_given = []
for _ in range(t):
    n_k = input()
    n_k_splits = n_k.split(" ")
    n = int(n_k_splits[0])
    k = int(n_k_splits[1])
    student_string = input()
    students = [int(s) for s in student_string.split(" ")]
    inputs_given.append((n, k, students))

for inp in inputs_given:
    n = inp[0]
    k = inp[1]
    students = inp[2]
    students_len = len(inp[2])
    students.sort()
    total_sum = 0
    for i in range(students_len - k + 1):
        if k == 1:
            total_sum += students[i]
        else:
            first = students[i]
            combinations = get_no_of_combinations_by_formula(students_len-i-1, k=k-1)
            total_sum += first * combinations
    print(total_sum)


# students = [25, 5, 15, 4, 0, 18, 7, 6, 17, 1, 18, 9, 5, 2]
# students.sort()
# k = 8
# total_sum = 0
# students_len = len(students)
# for i in range(students_len - k + 1):
#     if k == 1:
#         total_sum += students[i]
#     else:
#         first = students[i]
#         combinations = get_no_of_combinations_by_formula(students_len - i - 1, k=k - 1)
#         # print(first, combinations)
#         total_sum += first * combinations
#         print(total_sum)
#
# print(f"sum: {total_sum}")

