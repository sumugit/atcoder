S = input()

ans = []
if S.count(S[0]) == 1:
    print(S[0])
elif S.count(S[1]) == 1:
    print(S[1])
elif S.count(S[2]) == 1:
    print(S[2])
else:
    print(-1)
