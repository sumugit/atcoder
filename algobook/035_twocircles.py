import math

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())


def distance(a: list, b: list) -> float:
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

d = distance([x1, y1], [x2, y2])
if d < max(r1, r2) - min(r1, r2):
    print(1)
elif int(d) == max(r1, r2) - min(r1, r2):
    print(2)
elif r1 + r2 > d:
    print(3)
elif r1 + r2 == int(d):
    print(4)
elif r1 + r2 < d:
    print(5)

