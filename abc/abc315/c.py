N = int(input())
FS = [list(map(int, input().split())) for _ in range(N)]

FS.sort(key=lambda x: x[1], reverse=True)

ans, ans1, ans2 = -1, -1, -1
first_color = None
first_s = None
for i in range(N):
    f, s = FS[i]
    if first_color is None:
        first_color = f
        first_s = s
    else:
        if i == 1 and first_color != f:
            ans = first_s + s
            print(ans)
            exit()
        elif i == 1 and first_color == f:
            ans1 = first_s + s//2
        elif i > 1 and first_color != f:
            ans2 = first_s + s
            break

ans = max(ans1, ans2)
print(ans)