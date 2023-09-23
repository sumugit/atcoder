N, X = map(int, input().split())
A = list(map(int, input().split()))

A_sorted = sorted(A)
if sum(A_sorted[:-1]) >= X:
    ans = 0
elif A_sorted[0] <= X - sum(A_sorted[1:-1]) <= A_sorted[-1]:
    ans = X - sum(A_sorted[1:-1])
elif sum(A_sorted[1:]) >= X:
    ans = A_sorted[-1]
else:
    ans = -1
print(ans)