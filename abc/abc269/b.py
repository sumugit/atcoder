S = [list(input()) for _ in range(10)]

ans_lst = []

for i in range(10):
    temp = []
    for j in range(10):
        if S[i][j] == '#':
            temp.append((i, j))
    if len(temp) != 0:
        ans_lst.append(temp)

A = ans_lst[0][0][0] + 1
B = ans_lst[len(ans_lst)-1][0][0] + 1
C = ans_lst[0][0][1] + 1
D = ans_lst[0][len(ans_lst[0])-1][1] + 1
print(*[A, B])
print(*[C, D])