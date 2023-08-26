N = int(input())
A = list(map(int, input().split()))

A_sort = sorted(A)
for i in range(1, N):
    if A_sort[i-1] + 1 != A_sort[i]:
        print(A_sort[i-1] + 1)
        exit()