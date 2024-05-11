N = int(input())
H = list(map(int, input().split()))

h = H[0]
for i in range(1, N):
    if H[i] > h:
        print(i+1)
        exit()
print(-1)