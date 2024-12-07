from math import floor, sqrt
import bisect

N = int(input())

# 1) p^8 <= N
small_primes = [2,3,5,7,11,13,17,19,23,29,31,37]
count_p8 = 0
for p in small_primes:
    if p**8 <= N:
        count_p8 += 1

# 2): p^2*q^2 <= Nとなる(p,q)の組

# 素数列挙
MAX = sqrt(N)
is_prime = [True]*(int(MAX)+1)
is_prime[0], is_prime[1] = False, False
for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for k in range(i*i, int(MAX)+1, i):
            is_prime[k] = False
primes = [i for i in range(2, int(MAX)+1) if is_prime[i]]

# (p, q)
count_p2q2 = 0
for i, p in enumerate(primes):
    limit = MAX // p
    j = bisect.bisect_right(primes, limit) - 1
    if j > i:
        count_p2q2 += j - i

answer = count_p8 + count_p2q2
print(answer)
