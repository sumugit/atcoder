N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
ans = sum([abs(a-b) for a, b in zip(A, B)])
print(ans)