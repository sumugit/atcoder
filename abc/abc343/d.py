from collections import defaultdict

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(T)]
tmp = [0] * N
ans_dict = defaultdict(lambda: 0)
ans_dict[0] = N

ans = 1
for i in range(T):
    A, B = AB[i]
    tmp[A-1] += B
    if ans_dict[tmp[A-1]] == 0:
        ans += 1
    ans_dict[tmp[A-1]] += 1
    ans_dict[tmp[A-1]-B] -= 1
    if ans_dict[tmp[A-1]-B] == 0:
        ans_dict.pop(tmp[A-1]-B)
        ans -= 1
    print(ans)
