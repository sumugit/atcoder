N = int(input())
H = list(map(int, input().split()))

T = 0
for h in H:
    q, r = h // 5, h % 5
    T += q * 3
    while r > 0:
        T += 1
        r -= 3 if T % 3 == 0 else 1
print(T)