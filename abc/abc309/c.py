N, K = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

sort_ab = sorted(ab, key=lambda x: x[0], reverse=True)

sum_b = 0
for a, b in sort_ab:
    sum_b += b
    if sum_b > K:
        print(a+1)
        exit()
print(1)