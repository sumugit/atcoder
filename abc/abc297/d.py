A, B = map(int, input().split())
ans = 0

while True:
    if A == B:
        print(ans)
        break
    ### 無くてもよい ###
    elif A == 1:
        ans += B-1
        B = 1
    elif B == 1:
        ans += A-1
        A = 1
    ######
    elif A > B:
        ans += A//B
        A -= B*(A//B)
    else:
        ans += B//A
        B -= A*(B//A)
    # 0割り回避
    if A == 0 or B == 0:
        print(ans - 1)
        break
