# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/moody-numbers/

def get_digit_sum(num):
    total = 0
    while num // 10 != 0:
        total += num % 10
        num = num // 10
    total += num
    return total


def check_if_no_can_become_1(num):
    digit_sum = get_digit_sum(num)
    while digit_sum >= 10:
        digit_sum = get_digit_sum(digit_sum)
    return digit_sum in [1, 8]


def check_if_no_can_become_4(num):
    digit_sum = get_digit_sum(num)
    return num == 4 or digit_sum == 2


def check_if_no_can_become_1_or_4(num):
    return check_if_no_can_become_1(num) or check_if_no_can_become_4(num)


t = int(input())
numbers = []
for _ in range(t):
    number = int(input())
    numbers.append(number)

for n in numbers:
    res = "YES" if check_if_no_can_become_1_or_4(n) else "NO"
    print(res)
