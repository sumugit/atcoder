N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        temp = S[i] + S[j]
        if temp == temp[::-1]:
            print('Yes')
            exit()
        temp2 = S[j] + S[i]
        if temp2 == temp2[::-1]:
            print('Yes')
            exit()
print('No')