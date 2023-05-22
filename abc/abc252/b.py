N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flag = True
max = 0
max_list = []

for i in range(N):
    if A[i] > max:
        max = A[i]
        max_list = [i+1]
    elif A[i] == max:
        max_list.append(i+1)

for i in range(K):
    if B[i] in max_list:
        print("Yes")
        flag = False
        break

if flag:
    print("No")
