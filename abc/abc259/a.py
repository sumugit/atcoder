N, M, X, T, D = map(int, input().split())

a0 = T - D*X

if M <= X:
    print(a0 + D*M)
else:
    print(a0 + D*X)