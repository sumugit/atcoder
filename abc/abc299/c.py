N = int(input())
S = input()

ans_list = []
length = 0
idx = 0
while idx < N:
    if S[idx] == 'o':
        length += 1
        idx += 1
    else:
        ans_list.append(length)
        length = 0
        idx += 1
ans_list.append(length)
ans = max(ans_list)
if ans == N or ans == 0:
    print(-1)
else:
    print(ans)