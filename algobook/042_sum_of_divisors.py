N = int(input())

f = [0]*(N+1)
for i in range(1, N+1):
    for j in range(i, N+1, i):
        f[j] += 1
ans = 0
for i in range(1, N+1):
    ans += i*f[i]
print(ans)

"""
def eratosthenes(N: int) -> list:
    P = [True] * N
    P[0] = False
    for i in range(2, int(math.sqrt(N)+1)):
        for j in range(i+1, N+1): 
            if j%i == 0:
                P[j-1] = False
    ans = []
    for i in range(1, len(P)):
        if P[i]:
            ans.append(i+1)
    return ans

ans = 0
for n in range(1, N+1):
    prime_list = eratosthenes(n)
    cnt = 1
    n_star = n
    while n_star != 1:
        for prime in prime_list:
            temp_cnt = 0
            while n_star%prime == 0:
                temp_cnt += 1
                n_star /= prime
            cnt *= 1+temp_cnt
            if n_star == 1:
                break
    # print(n, cnt)
    ans += n*cnt

print(ans)
"""
