r, c = map(int, input().split())
a = [[int(i) for i in input().split()] for _n in range(2)]

print(a[r-1][c-1])