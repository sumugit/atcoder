N, M = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
A += A

c = [0] * M
d, ans = 0, 0
for i in range(2 * N):
    if i >= N:
        c[(d - s) % M] -= 1
        # Mで割った余りが同じ累積和の差はMの倍数
        # 逐次計算のため組み合わせを計算する必要はない
        # (これまでのc[d%M]の個数をそのままカウントすればよい)
        ans += c[d % M]
    c[d % M] += 1
    d += A[i]
print(ans)