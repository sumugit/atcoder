N, K = map(int, input().split())
S = list(input())

cnt = 0
flag = True
while flag:
    flag = False
    for i in range(N-K+1):
        if sum([1 if val == 'O' else 0 for val in S[i:i+K]]) == K:
            for j in range(K):
                S[i+j] = 'X'
            cnt += 1
            flag = True
print(cnt)