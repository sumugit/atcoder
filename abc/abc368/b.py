N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    A = sorted(A, reverse=True)
    if A[0] > 0 and A[1] > 0:
        A[0] = A[0] - 1
        A[1] = A[1] - 1
        ans += 1
    else:
        break
print(ans)