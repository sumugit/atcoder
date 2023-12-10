N, M = map(int, input().split())
S = list(input())

ans = 0
rest_a = 0
rest_m = M
for i in range(N):
    if S[i] == '0':
        rest_a = ans
        rest_m = M
    elif S[i] == '1':
        if rest_m > 0:
            rest_m -= 1
        else:
            if rest_a > 0:
                rest_a -= 1
            else:
                ans += 1
    elif S[i] == '2':
        if rest_a > 0:
            rest_a -= 1
        else:
            ans += 1

print(ans)