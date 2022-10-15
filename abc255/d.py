# ソート, 累積和, 二分探索
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
rw = [0] * (N+1)
# 累積和
for i in range(N):
    rw[i+1] = rw[i] + A[i]
X = []
for i in range(Q):
    X.append(int(input()))


for i in range(Q):
    s = 0
    e = N-1
    while s <= e:
        t = int((s+e)/2)
        if A[t]<X[i]:
            s = t+1
        else:
            e = t-1
    # end for
    # Ai の sum 展開後の各項
    res = X[i]*s # k*x
    res -= rw[e+1]
    res += rw[N] - rw[s]
    res -= X[i]*(N-s)
    print(res)