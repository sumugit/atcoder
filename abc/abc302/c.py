from itertools import permutations

N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(list(input()))

for v in permutations(range(N), N):
    flag = True
    for i in range(N-1):
        cnt = 0
        for j in range(M):
            if S[v[i]][j] != S[v[i+1]][j]:
                cnt += 1
                if cnt > 1:
                    break
        if cnt != 1:
            flag = False
            break
    if flag:
        print("Yes")
        exit()
print("No")