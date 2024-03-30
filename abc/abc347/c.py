def testcase():
    N, A, B = map(int, input().split())
    D = list(map(int, input().split()))
    for i in range(N):
        D[i] %= (A + B)
    D.sort()
    D.append(D[0] + (A + B))
    ok = False
    for i in range(N):
        # 全部がB未満の時のみ、必ず条件を満たさないと言える
        # それ以外の場合、条件を満たす可能性がある
        if D[i + 1] - D[i] - 1 >= B:
            ok = True
    print("Yes" if ok else "No")

testcase()