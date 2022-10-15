N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

expected = 0.0
for i in range(len(A)):
    expected += (1/3)*A[i] + (2/3)*B[i]

print(expected)