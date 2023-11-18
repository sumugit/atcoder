N, L = map(int, input().split())
AB = [list(input().split()) for _ in range(N)]

# 人を区別しないで考える
ans = 0
for i in range(N):
    a = int(AB[i][0])
    b = AB[i][1]
    if b == 'E':
        ans = max(ans, L-a)
    else:
        ans = max(ans, a)

print(ans)