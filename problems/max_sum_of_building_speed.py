# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/maximum-sum-of-building-speed-00ab8996/


n = int(input())
s = input()
splits = s.split(" ")
workers = [int(w) for w in splits]
workers = sorted(workers, reverse=True)

max_value_sum = 0
for i in range(1, 2*n, 2):
    max_value_sum += workers[i]

print(max_value_sum)
