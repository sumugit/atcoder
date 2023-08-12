N = int(input())
S = input()
Q = int(input())
txc = [list(map(str, input().split())) for _ in range(Q)]

# 逆から見ていく
t_23 = -1
t_23_i = -1
for i in range(Q-1, -1, -1):
    t, x, c = txc[i]
    t, x = int(t), int(x)
    if t == 2 or t == 3:
        t_23 = t
        t_23_i = i
        break

if t_23 == 2:
    S = S.lower()
elif t_23 == 3:
    S = S.upper()

S = list(S)

for i in range(Q):
    t, x, c = txc[i]
    t, x = int(t), int(x)
    
    if t == 1:
        if i <= t_23_i:
            if t_23 == 2:
                c = c.lower()
            elif t_23 == 3:
                c = c.upper()
        S[x-1] = c

print(*S, sep='')