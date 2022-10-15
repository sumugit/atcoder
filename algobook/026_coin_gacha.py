N = int(input())
expected = 0
for r in range(N):
    expected += N/(N-r)

print(expected)