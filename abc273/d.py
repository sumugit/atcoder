H, W, rs, cs = map(int, input().split())
# map = [['.'*W] for _ in range(H)]
N = int(input())
rc = []
for _ in range(N):
    rc_input = list(map(input().split()))
    rc.append(rc_input)
    map[rc_input[0]-1][rc_input[1]-1] = '#'
Q = int(input())
dl = []
for _ in range(Q):
    dl.append(list(map(int, input().split())))

now = map[rs-1][cs-1]
for q in range(Q):
    dl[q]