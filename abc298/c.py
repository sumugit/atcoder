import heapq
from collections import defaultdict

N = int(input())
Q = int(input())
queries = [list(input().split()) for _ in range(Q)]
boxes = [[] for _ in range(N)]
nums = [set() for _ in range(2*10**5)]

for q in queries:
    label = q[0]
    if label == '1':
        num = q[1]
        box = q[2]
        boxes[int(box)-1].append(int(num))
        nums[int(num)-1].add(int(box))
        # heapq.heappush(boxes[box], int(num))
        # heapq.heappush(nums[num], int(box))
    elif label == '2':
        box = q[1]
        ans = sorted(boxes[int(box)-1])
        print(*ans)
        # ans = boxes[box].copy()
        # print(*[heapq.heappop(ans) for _ in range(len(ans))])
    elif label == '3':
        num = q[1]
        ans = sorted(nums[int(num)-1])
        print(*ans)
        # ans = nums[num].copy()
        # print(*set([heapq.heappop(ans) for _ in range(len(ans))]))


