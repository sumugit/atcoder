N = int(input())
A = list(map(int, input().split()))
NUMBER = 1000000007

def modpow(a: int, b: int, m: int, lim: int) -> int:
    """ 
    繰り返し二乗法 O(logb)
    a^b を mod で割った余りを出力
    lim : mod で割る数を2進数にした時の桁数 (10^3 ~ 2^10)
    """
    p = a
    ans = 1
    for i in range(lim):
        if b & (1 << i) != 0:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

ans = 0
for i in range(len(A)):
    if i==0:
        ans += A[i]%NUMBER
    else:
        ans += A[i]*modpow(2, i, NUMBER, 20)%NUMBER
print(ans%NUMBER)