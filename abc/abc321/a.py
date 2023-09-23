N = input()
if len(N) == 1:
    print("Yes")
else:
    for i in range(1, len(N)):
        if N[i-1] <= N[i]:
            print("No")
            exit()
    print("Yes")