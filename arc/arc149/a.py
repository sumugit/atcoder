N, M = map(int, input().split())
ori_val = 0
flag = False
mod_a = {}
# 効率的に余りを計算
for a in range(1, 10):
    mod_a[a] = a%M

for n in range(N):
    # ori_val = 10*(ori_val) + 1
    for a in range(1, 10):
        if n == 0:
            quo = mod_a[a]
        else:
            quo = (10*mod_a[a] + a)%M
        if quo == 0:
            flag = True
            max_a, max_n = (a, n+1) # 必要な情報のみ保存 (桁の増大による無駄な計算量を防ぐ)
        mod_a[a] = quo  # 桁の増大を防ぐため余りで考える
if not flag:
    print(-1)
else:
    print(int(str(max_a)*(max_n)))