import itertools
import copy

N, M = map(int, input().split())

num_list = list(range(1, M+1))

for num in range(1, M-N+2):
    temp = copy.copy(num_list)
    temp.remove(num)
    for v in itertools.permutations(temp, N-1):
        ans = [num] + list(v)
        flag = False
        for i in range(1, len(ans)):
            if ans[i] - ans[i - 1] <= 0:
                flag = True
                break
        if not flag:
            print(*ans)
