N, M, K = map(int, input().split())
CAR = [list(input().split()) for _ in range(M)]

ans = 0
for bit in range(1 << N): # 2^N
    flag = [False] * M
    for i, car in enumerate(CAR):
        C, A, R = int(car[0]), list(map(lambda x: int(x)-1, car[1:-1])), car[-1]
        cnt = 0
        for a in A:
            if (bit & (1 << a)) != 0: # == 1 ではない
                cnt += 1
        if (R == 'o' and cnt >= K) or (R == 'x' and cnt < K):
            flag[i] = True
    if all(flag):
        ans += 1
print(ans)