T = int(input())
N = int(input())
A = [0 for _ in range(T+1)]

for i in range(N):
    L, R = map(int, input().split())
    A[L] += 1
    A[R] -= 1

B = [A[0]]
for i in range(1, T+1):
    B.append(B[i-1]+A[i])

for i in range(T):
    print(B[i])
