N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [[a, b] for a, b in zip(A, B)]
AB_sortby_A = sorted(AB, key=lambda x: x[0], reverse=True)
AB_sortby_B = sorted(AB, key=lambda x: x[1], reverse=True)

ans = 2*10e14

cumX, cumY = 0, 0
cnt = 0
for ab in AB_sortby_A:
    a, b = ab
    cumX += a
    cumY += b
    cnt += 1
    if cumX > X or cumY > Y:
        break
ans = min(ans, cnt)

cumX, cumY = 0, 0
cnt = 0
for ab in AB_sortby_B:
    a, b = ab
    cumX += a
    cumY += b
    cnt += 1
    if cumX > X or cumY > Y:
        break
ans = min(ans, cnt)

print(ans)