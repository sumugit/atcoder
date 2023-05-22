N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(len(A)-1):
    if abs(A[i] - A[i+1]) != 1:
        if A[i] > A[i+1]:
            for a in range(A[i], A[i+1], -1):
                ans.append(a)
        else:
            for a in range(A[i], A[i+1]):
                ans.append(a)
    else:
        ans.append(A[i])
ans.append(A[-1])

print(*ans, sep=' ')