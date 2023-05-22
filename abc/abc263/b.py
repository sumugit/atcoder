N = int(input())
P = list(map(int, input().split()))

val = N
ans = 0
while val != 1:
    val = P[val-2]
    ans += 1

print(ans)