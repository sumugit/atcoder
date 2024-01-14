N = int(input())
N_bin = bin(N)[2:]
ans = 0
for i in range(len(N_bin), 0, -1):
    if N_bin[i-1] == '1':
        break
    ans += 1
print(ans)