N, K = map(int, input().split())
S = list(input())

cnt_1 = S.count('1')
cnt_0 = S.count('0')
if K%2 == 0 and cnt_1%2 == 1:
    print('No')
elif K%2 == 1 and cnt_1%2 == 0:
    print('No')
else:
    if K > cnt_1 and cnt_0 > K-cnt_1:
        print('Yes')
    elif K <= cnt_1:
        print('Yes')
    else:
        print('No')