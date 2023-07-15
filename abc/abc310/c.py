from collections import Counter, deque, defaultdict

N = int(input())
S = [input() for _ in range(N)]

dict_a = defaultdict(lambda: False)
for i in range(N):
    s = S[i]
    s_rev = s[::-1]
    if not dict_a[s] and not dict_a[s_rev]:
        dict_a[s] = True

ans = 0
for key in dict_a.keys():
    if dict_a[key]:
        ans += 1
print(ans)