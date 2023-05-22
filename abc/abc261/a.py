L1, R1, L2, R2 = map(int, input().split())

road = [0] * 100

for i in range(L1, R1):
    road[i] += 1
for i in range(L2, R2):
    road[i] += 1

print(road.count(2))
