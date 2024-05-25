A, B = map(int, input().split())
ans = [1, 2, 3]
if A == B:
    print(-1)
else:
    ans.remove(A)
    ans.remove(B)
    print(ans[0])