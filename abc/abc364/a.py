N = int(input())
S = [input() for _ in range(N)]

for i in range(N-1):
    if S[i] == 'sweet' and S[i] == S[i+1] and i != N-2:
        print('No')
        exit()
print('Yes')
