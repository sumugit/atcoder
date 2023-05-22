N = int(input())
A = list(map(int, input().split()))
ans = [0]*(2*N+2)
for idx in range(1, len(A)+1):
    ans[2*(idx)] = ans[A[idx-1]] + 1
    ans[2*(idx)+1] = ans[A[idx-1]] + 1
for i in range(1,2*N+2):
    print(ans[i])