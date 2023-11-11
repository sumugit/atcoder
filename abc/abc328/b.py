N = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(N):
    set_mmdd = set()
    set_mmdd |= set(list(str(i+1)))
    for j in range(D[i]):
        temp_mmdd = set_mmdd.copy()
        temp_mmdd |= set(list(str(j+1)))
        if len(temp_mmdd) == 1:
            ans += 1
print(ans)