A, B, C = map(int, input().split())

sleep = [False] * 25
if C < B:
    C += 24
for slp in range(B, C+1):
    sleep[slp%25] = True

if not sleep[A]:
    print('Yes')
else:
    print('No')