N, K = map(int, input().split())
A = list(map(int, input().split()))

boxes = 0
start = 0
for i in range(N):
    if boxes + A[i] <= K:
        boxes += A[i]
    else:
        start += 1
        boxes = A[i]

print(start+1)