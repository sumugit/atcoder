N = int(input())
P = list(map(int, input().split()))
s = sorted(P)

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

k = 0
temp = s.copy()
# k を求める
for idx, p in enumerate(P):
    digit = N-idx
    for num in temp:
        if num == p:
            temp.remove(num)
            break
        else:
            k += factorial(digit-1)
k += 1
target = k-1
ans = []
k_cnt = 0
while len(s)>0:
    for idx, num in enumerate(s):
        digit = len(s)
        fct = factorial(digit-1)
        if k_cnt + fct < target:
            k_cnt += fct
        else:
            ans.append(num)
            s.remove(num)
            break
print(*ans)
