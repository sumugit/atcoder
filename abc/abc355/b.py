N, M = map(int, input().split())
A = [[n, 'A'] for n in list(map(int, input().split()))]
B = [[n, 'B'] for n in list(map(int, input().split()))]

C = sorted(A + B, key=lambda x: x[0])
for i in range(1, len(C)):
    if C[i-1][1] == C[i][1] == 'A':
        print('Yes')
        exit()
print('No')
