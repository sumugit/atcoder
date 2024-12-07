N = int(input())
TV = [list(map(int, input().split())) for _ in range(N)]

time_now = TV[0][0]
tank = TV[0][1]
for i in range(1, N):
    delta_time = TV[i][0] - time_now
    tank -= delta_time
    if tank < 0:
        tank = 0
    tank += TV[i][1]
    time_now = TV[i][0]
print(tank)