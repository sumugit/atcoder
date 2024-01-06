N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

nim_sum = (AB[0][0]-1) ^ (AB[0][1]-1)
for i in range(1, N):
    nim_sum ^= (AB[i][0]-1) ^ (AB[i][1]-1)
if nim_sum == 0:
    print("Second")
else:
    print("First")
