N, Q = map(int, input().split())
S = list(input())
lr = [list(map(int, input().split())) for _ in range(Q)]

cumlist = [0] * (N+1)
for i in range(N-1):
    if S[i] == S[i+1]:
        cumlist[i+1] = cumlist[i] + 1
    else:
        cumlist[i+1] = cumlist[i]

for i in range(Q):
    print(cumlist[lr[i][1]-1] - cumlist[lr[i][0]-1])