N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

# 尺取法
y, z, w = 0, 0, 0
s0, s1, s2 = 0, 0, 0
ok = 0
for x in range(N):
    while y < N and s0 < P:
        s0 += A[y]
        s1 -= A[y]  # s1 は引いた分後で足す
        y += 1
    while z < N and s1 < Q:
        s1 += A[z]
        s2 -= A[z]  # s2 は引いた分後で足す
        z += 1
    while w < N and s2 < R:
        s2 += A[w]
        w += 1
    if s0 == P and s1 == Q and s2 == R:
        ok = 1
        break
    s0 -= A[x]  # x を左から右にずらす

print('Yes' if ok else 'No')
