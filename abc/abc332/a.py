N, S, K = map(int, input().split())
PQ = [list(map(int, input().split())) for _ in range(N)]

cost = 0
for i in range(N):
    P, Q = PQ[i]
    cost += P*Q

if cost < S:
    cost += K

print(cost)