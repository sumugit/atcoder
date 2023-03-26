A, B, C = map(int, input().split())
MOD = 998244353
sum1 = (A*(A+1)//2)%MOD
sum2 = (B*(B+1)//2)%MOD
sum3 = (C*(C+1)//2)%MOD

ans = (sum1 * sum2 * sum3)%MOD
print(ans)