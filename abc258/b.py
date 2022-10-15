N = int(input())
A = []

a_max = 0
start = []
dir = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]

for n1 in range(N):
    a = list(map(int, input()))
    for n2 in range(N):
        a_max = max(a[n2], a_max)
    A.append(a)

for n1 in range(N):
    for n2 in range(N):
        if A[n1][n2] == a_max:
            start.append([n1, n2])

maxnum = 0
for d in dir:
    for s in start:
        # 参照渡し注意
        now = s.copy()
        sum = str(A[s[0]][s[1]])
        for n in range(N-1):
            if now[0] + d[0] < 0:
                now[0] = N-1
            elif now[0] + d[0] > N-1:
                now[0] = 0
            else:
                now[0] += d[0]
            
            if now[1] + d[1] < 0:
                now[1] = N-1
            elif now[1] + d[1] > N-1:
                now[1] = 0
            else:
                now[1] += d[1]

            sum += str(A[now[0]][now[1]])
        maxnum = max(maxnum, int(sum))

print(str(maxnum))
