N = int(input())
A = list(map(int, input().split()))

def prod(n: int) -> int:
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def my_conb(n: int, r: int) -> int:
    ans = int(prod(n) / (prod(n-r) * prod(r)))
    return ans

a = A.count(1)
b = A.count(2)
c = A.count(3)

ans_a = int((a*(a-1))/2)
ans_b = int((b*(b-1))/2)
ans_c = int((c*(c-1))/2)

print(ans_a + ans_b + ans_c)
