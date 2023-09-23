ans = []
# Generate 321-like Numbers
for i in range(2, 1 << 10):  # 1 << 10 equals 1024
    x = 0
    for j in range(9, -1, -1):
        if i & (1 << j): # i の j ビット目が 1 かどうかを判定
            x = x * 10 + j # j ビット目自体を足すことで, 321-like Number を生成できる
    ans.append(x)

ans.sort()

k = int(input())
print(ans[k - 1])
