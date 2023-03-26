N = int(input())
MOD = 1000000007
sum1 = (N*(N+1)//2)%MOD
ans = (sum1 * sum1)%MOD

print(ans)