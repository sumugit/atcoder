a, b, c, d, e, f = map(int, input().split())
mod = 998244353
a %=mod; b%=mod; c%=mod; d%=mod; e%=mod; f%=mod
abc = (((a*b)%mod)*c)%mod
def_ = (((d*e)%mod)*f)%mod
ans = (abc-def_)%mod
print(ans)
