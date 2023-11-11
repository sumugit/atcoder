N, K = map(int, input().split())

if K < 2*N-2:
    print("No")
else:
    rem = K-(2*N-2)
    if rem%2 == 0:
        print("Yes")
    else:
        print("No")