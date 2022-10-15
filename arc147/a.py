from collections import deque

N = int(input())
A = list(map(int, input().split()))

sorted_a = deque(sorted(A))
cnt = 0


max_a = sorted_a[-1]
min_a = sorted_a[0]
while len(sorted_a) != 1:
    if min_a == 1:
        cnt += len(sorted_a)-1
        break
    max_a_val = max_a%min_a
    cnt += 1
    if max_a_val == 0:
        sorted_a.pop()
        # sorted_a = sorted_a[:-1]  # O(N)
        max_a = sorted_a[-1]
    else:
        sorted_a.pop()
        # sorted_a = sorted_a[:-1]  # O(N)
        sorted_a.appendleft(max_a_val)
        # sorted_a = [max_a_val] + sorted_a  # O(N)
        min_a = max_a_val
        max_a = sorted_a[-1]

print(cnt)