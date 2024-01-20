N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

x = 0
y = 0
for i in range(N):
    x += XY[i][0]
    y += XY[i][1]
if x > y:
    print('Takahashi')
elif x == y:
    print('Draw')
else:
    print('Aoki')