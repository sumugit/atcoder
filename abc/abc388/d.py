# N = int(input())
# A = list(map(int, input().split()))

# B = [0]*N
# D = [0]*N
# for i in range(N):
#     B[i] = A[i]+ 2*i-N+1
#     if i+A[i]+i+1 < N:
#         D[i+A[i]+i+1] += 1

# for i in range(N-1):
#     D[i+1] += D[i]
# for i in range(N):
#     B[i] = max(0, B[i]-D[i])
# print(*B)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0]*n
    d = [0]*(n+1)

    for i in range(n):
        if i != 0:
            # 累積和 (imos法)
            c[i] = c[i-1] + d[i] # d[i]は石を更に受け取るか、あるいは他の成人者が石を全て使い切って1減るか
            a[i] += c[i]

        cnt = min(n-i-1, a[i]) # i+1以降に渡す石の数の合計
        a[i] -= cnt
        d[i+1] += 1 # i+1は成人になるとiから1個石をもらう
        d[min(n, i+cnt+1)] -= 1 #iが渡せる石より成人になるのが遅い人 (右端+1)

    print(" ".join(map(str, a)))

if __name__ == "__main__":
    main()
