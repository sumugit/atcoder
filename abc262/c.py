N = int(input())
a = [0] + list(map(int, input().split()))

num_conb = 0
ans = 0
for i in range(1, N+1):
    if a[i] == i:
        num_conb += 1
    elif a[i] != i and i < a[i]:
        if a[a[i]] == i:
            ans += 1

ans += int(num_conb*(num_conb-1)/2)
print(ans)

