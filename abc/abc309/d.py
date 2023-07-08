from collections import deque, defaultdict
NUM = 10**9 + 7

N1, N2, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

graph_g1 = defaultdict(lambda: [])
graph_g2 = defaultdict(lambda: [])
for a, b in ab:
    if a <= N1:
        graph_g1[a].append(b)
        graph_g1[b].append(a)
    if a > N1:
        graph_g2[a].append(b)
        graph_g2[b].append(a)

g1_cost = defaultdict(lambda: NUM)
cost = 1
g1_cost[1] = 0
next_pos = deque(graph_g1[1])
while len(next_pos) != 0:
    temp = deque()
    for pos in next_pos:
        now_cost = min(g1_cost[pos], cost)
        if now_cost < g1_cost[pos]:
            g1_cost[pos] = now_cost
            for nps in graph_g1[pos]:
                temp.append(nps)
    cost += 1
    next_pos = temp

g2_cost = defaultdict(lambda: NUM)
cost = 1
g2_cost[N1+N2] = 0
next_pos = deque(graph_g2[N1+N2])
while len(next_pos) != 0:
    temp = deque()
    for pos in next_pos:
        now_cost = min(g2_cost[pos], cost)
        if now_cost < g2_cost[pos]:
            g2_cost[pos] = now_cost
            for nps in graph_g2[pos]:
                temp.append(nps)
    cost += 1
    next_pos = temp

g1_cost_max = max(g1_cost.values())
g2_cost_max = max(g2_cost.values())
ans = g1_cost_max + 1 + g2_cost_max
print(ans)