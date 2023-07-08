A, B = map(int, input().split())
A, B = min(A, B), max(A, B)

if abs(A-B) == 1 and A%3 != 0:
    print("Yes")
else:
    print("No")