N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

for i in range(N):
    ans = -1
    max_dist = -1
    for j in range(N):
        if i == j: continue
        tmp_dist = max_dist
        max_dist = max(max_dist, dist(XY[i], XY[j]))
        if tmp_dist != max_dist:
            ans = j+1
    print(ans)