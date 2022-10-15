import collections

N = int(input())
a = list(map(int, input().split()))
a = sorted(a)
b = sorted(list(set(a)))
i = 0
j = N-1
k = 0
now = 0
ans = 0
while i <= j:
    if k < len(b):
        temp = b[k]
    if temp == now + 1:
        ans += 1
        now += 1
        k += 1
        i += 1
    else:
        if i < j:
            ans += 1
            now += 1
            j -= 2
        else:
            break

print(ans)