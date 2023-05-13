S, N = list(reversed(input())), int(input())
s = 0
for i in range(len(S)):
    # bit 演算しているが結果は 10 進数であることに注意
    s |= (S[i] == '1') << i
if s > N:
    print(-1)
else:
    for i in reversed(range(len(S))):
        # (s | 1 << i) は s の i 桁目を 1 にする (s と 1 << i の論理和)
        if S[i] == '?' and (s | 1 << i) <= N:
            s |= 1 << i
    print(s)