"""
解答のポイント: 長さ N の非負整数列の mex は 0 以上 N 以下である！
"""

n, q = map(int, input().split())
bk = [0] * (n + 1)
a = list(map(int, input().split()))

for num in a:
    if num <= n:
        bk[num] += 1

st = set(i for i in range(n + 1) if bk[i] == 0)

for _ in range(q):
    i, x = map(int, input().split())
    i -= 1  # インデックスを0ベースに調整

    if a[i] <= n:
        bk[a[i]] -= 1
        if bk[a[i]] == 0:
            st.add(a[i])

    a[i] = x
    if a[i] <= n:
        if bk[a[i]] == 0:
            st.remove(a[i])
        bk[a[i]] += 1

    print(min(st))  # stの最小値を出力
