N = int(input())
S = [input() for i in range(N)]

ans = 0
for s in S:
    if s == "Takahashi":
        ans += 1
print(ans)