S = input()
T = input()

# O(|S| + |T|)
# ランレングス圧縮
# 文字列として格納するのでは無く, 配列として格納する

if len(S) > len(T):
    print('No')
    exit()

if S == T:
    print('Yes')
    exit()

flg = False
cnt = 0
s0 = ''
t0 = ''
s1 = []
t1 = []
for i in range(len(S)):
    if i == len(S) - 1:
        s0 += S[i]
        if flg:
            cnt += 1
            s1.append(cnt)
            cnt = 0
        else:
            s1.append(1)
    elif S[i] != S[i+1]:
        s0 += S[i]
        if flg:
            cnt += 1
            s1.append(cnt)
            flg = False
            cnt = 0
        else:
            s1.append(1)
    else:
        flg = True
        cnt += 1

flg = False
cnt = 0

for j in range(len(T)):
    if j == len(T) - 1:
        t0 += T[j]
        if flg:
            cnt += 1
            t1.append(cnt)
            cnt = 0
        else:
            t1.append(1)
    elif T[j] != T[j+1]:
        t0 += T[j]
        if flg:
            cnt += 1
            t1.append(cnt)
            flg = False
            cnt = 0
        else:
            t1.append(1)
    else:
        flg = True
        cnt += 1


if (s0 == t0):
    for i in range(len(s1)):
        if s1[i] == t1[i]:
            pass
        elif (s1[i] < t1[i]) and (s1[i] >= 2):
            pass
        else:
            print('No')
            exit()
    print('Yes')    
else:
    print('No')