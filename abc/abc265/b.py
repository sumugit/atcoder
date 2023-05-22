N, M, T = map(int, input().split())
A = list(map(int, input().split()))
X = []
Y = []
for m in range(M):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

t = T
m_idx = 0
for i in range(N-1):
    t -= A[i]
    if t <= 0:  # 0 '以下'
        print('No')
        exit()
    if len(X) > 0:
        if i+1 == X[m_idx]-1 and i+1 <= N-2:
            t += Y[m_idx]
            if m_idx <= M-2:
                m_idx += 1

print('Yes')