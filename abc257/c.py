import numpy as np
import collections

N = int(input())
S = input()
W = list(map(int, input().split()))
W_dict = collections.Counter(W)
W_index_sort = np.argsort(W)
ans = 0

for i in range(N+1):
    if i == 0:
        ans_max = S.count('1')
    elif i == N:
        ans_max = S.count('0')
    else:
        x = (W[W_index_sort[i-1]] + W[W_index_sort[i]])/2
        # 値が等しい場合は数字変えない
        if W[W_index_sort[i-1]] < x:
            if S[W_index_sort[i-1]:W_index_sort[i-1]+1] == '0':
                ans_max += 1
            else:
                ans_max -= 1
    
    ans = max(ans_max, ans)
    
print(ans)