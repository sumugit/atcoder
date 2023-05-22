N, X = map(int, input().split())

alb = [chr(ord("A")+i) for i in range(26)]

cnt = 0
for a in alb:
    for _itr in range(N):
        ans = a
        cnt += 1
        if cnt == X:
            print(ans)
            exit()