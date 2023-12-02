N = int(input())
A = list(map(int, input().split()))
reversed_A = sorted(A, reverse=True)

cumulative_sum = 0

sum_dict = {}
prev = None
for a in reversed_A:
    now = a
    if prev != now: 
        sum_dict[a] = cumulative_sum
    prev = a
    cumulative_sum += a

ans = []
for a in A:
    ans.append(sum_dict[a])
print(*ans, sep=' ')