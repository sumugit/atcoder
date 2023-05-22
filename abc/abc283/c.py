S = list(input())
zero_cnt = 0
now = S[0]
i = 1
if len(S) == 1:
    print(1)
else:
    while i < len(S):
        if now == '0' and S[i] == '0':
            zero_cnt += 1
            i += 1
        if i+1 < len(S):
            now = S[i]
        i += 1
    ans = len(S) - zero_cnt
    print(ans)