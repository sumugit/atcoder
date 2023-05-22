N, K = map(int, input().split())
A = list(map(int, input().split()))

# しゃくとり法
left = 0
right = 0
ans = 0 # 差がK以下になる選び方の数
# 差がK以下になるまでrightを進める
while right < N:
    if A[right] - A[left] <= K:
        ans += right - left # Aはソート済みなので、leftを固定したときのrightの選び方はright-left通り
        right += 1
    else:
        left += 1

print(ans)