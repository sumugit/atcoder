from collections import deque, defaultdict

N, K = map(int, input().split())
g_a = defaultdict(lambda: [])
for i in range(N):
    a_input = list(map(int, input().split()))
    for j in range(N):
        if a_input[j] != 0:
            g_a[i].append(j)
Q = int(input())
st = [list(map(int, input().split())) for _ in range(Q)]

for s, t in st:
    start = (s-1)%N
    end = (t-1)%N
    queue = deque([start])
    trace = defaultdict(lambda: -1)
    trace[start] = 0
    flag = False
    while len(queue) > 0:
        val = queue.popleft()
        adj_i = g_a[val]
        # i の隣接ノード
        for j in adj_i:
            if trace[j] == -1:
                if j == end:
                    print(trace[val] + 1)
                    flag = True
                    break
                queue.appendleft(j)
                trace[j] = trace[val] + 1
        if flag:
            break
    if not flag:
        print(-1)