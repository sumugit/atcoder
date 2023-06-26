N = int(input())
A = list(map(int, input().split()))

max1 = max(A)
A.remove(max1)
max2 = max(A)
print(max1 + max2)