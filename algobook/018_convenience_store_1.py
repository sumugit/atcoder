N = int(input())
A = list(map(int, input().split()))

a = A.count(100)
b = A.count(400)
c = A.count(200)
d = A.count(300)
print(a*b + c*d)