# https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/roy-and-shopping-20/


# def get_smallest_divisor(n):
#     least_prime_numbers = [0]*(n+1)
#     least_prime_numbers[1] = 1
#
#     for i in range(2, n+1):
#         if n % i == 0:
#             pass
#
#     # if divisible by 2
#     if n % 2 == 0:
#         return 2
#
#     # iterate from 3 to sqrt(n)
#     i = 3
#     while i*i <= n:
#         if n % i == 0:
#             return i
#         i += 2
#
#     return n


def get_smallest_divisor(n):
    # Create a vector to store least primes.
    # Initialize all entries as 0.
    least_prime = [0] * (n + 1)

    # We need to print 1 for 1.
    least_prime[1] = 1

    for i in range(2, n + 1):

        # least_prime[i] == 0
        # means it i is prime
        if (least_prime[i] == 0):

            # marking the prime number
            # as its own lpf
            least_prime[i] = i

            # mark it as a divisor for all its
            # multiples if not already marked
            for j in range(i * i, n + 1, i):
                if (least_prime[j] == 0):
                    least_prime[j] = i

    # print least prime factor
    # of numbers till n
    return least_prime[n]


t = int(input())
input_list = []
for ct in range(t):
    input_list.append(int(input()))


for inp in input_list:
    print(inp - get_smallest_divisor(inp))
