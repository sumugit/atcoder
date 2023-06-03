N = int(input())

if N <= 1e3-1:
    print(N)
elif N <= 1e4-1:
    print(N//10 * 10)
elif N <= 1e5-1:
    print(N//100 * 100)
elif N <= 1e6-1:
    print(N//1000 * 1000)
elif N <= 1e7-1:
    print(N//10000 * 10000)
elif N <= 1e8-1:
    print(N//100000 * 100000)
elif N <= 1e9-1:
    print(N//1000000 * 1000000)