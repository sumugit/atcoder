N = int(input())

m = 1
while m<=N+1:
    if m == N+1:
        print('Second')
        exit(0)
    m *= 2
print('First')