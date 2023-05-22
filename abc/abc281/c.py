N, T = map(int, input().split())
A = list(map(int, input().split()))

sum_a = sum(A)
rest_time = T%sum_a
time = 0
for i in range(len(A)):
    if time + A[i] <= rest_time:
        time += A[i]
    else:
        ans = rest_time - time
        print(i+1, ans)
        break