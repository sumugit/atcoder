N = int(input())
A = list(map(int, input().split()))

nim_sum = 0
for i in range(N):
    nim_sum ^= A[i]

if nim_sum == 0:
    print('Second')
else:
    print('First')