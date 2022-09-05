# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/special-sum-3/

def get_divisor_sum(n):
    # https://cp-algorithms.com/algebra/phi-function.html#etf_1_to_n
    return n


t = int(input())
input_list = []
for ct in range(t):
    inp = int(input())
    input_list.append(inp)


for inp in input_list:
    print(get_divisor_sum(inp))
