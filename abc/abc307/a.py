N = int(input())
A = list(map(int, input().split()))

walks = []
sum_a = 0
for i, a in enumerate(A):
    sum_a += a
    if (i+1)%7 == 0:
        walks.append(sum_a)
        sum_a = 0
print(*walks)