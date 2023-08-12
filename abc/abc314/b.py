N = int(input())
C = []
A = []
for i in range(N):
    c = int(input())
    a = list(map(int, input().split()))
    C.append(c)
    A.append(a)
X = int(input())

min_c = 38
ans = []

for i in range(N):
    if X in A[i]:
        if C[i] < min_c:
            min_c = C[i]
            ans = [i+1]
        elif C[i] == min_c:
            ans.append(i+1)

ans = sorted(ans)

print(len(ans))
print(*ans)
