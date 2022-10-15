N = int(input())
A = list(map(int, input().split()))
sum_A = [A[0]]
for i in range(1, N-1):
    sum_A.append(sum_A[i-1]+A[i])
sum_A = [0] + sum_A
M = int(input())

Bm_1 = int(input())
ans = 0
for m in range(2, M+1):
    Bm_2 = int(input())
    ans += abs(sum_A[Bm_2-1]-sum_A[Bm_1-1])
    Bm_1 = Bm_2

print(ans)