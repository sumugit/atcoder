N = int(input())
A = [list(input()) for _ in range(N)]

flag = True

for i in range(N):
    for j in range(N):
        if A[i][j] == 'W' and A[j][i] != 'L':
            flag = False
            break
        elif A[i][j] == 'L' and A[j][i] != 'W':
            flag = False
            break
        elif A[i][j] == 'D' and A[j][i] != 'D':
            flag = False
            break
    if not flag:
        break

if flag:
    print("correct")
else:
    print("incorrect")