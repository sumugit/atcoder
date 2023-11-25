import math

D = int(input())

min_diff = float('inf')
for x in range(int(math.sqrt(D)) + 2):
    y2 = D - x*x
    if y2 >= 0:
        y = int(math.sqrt(y2))
        diff = abs(x*x + y*y - D)
        min_diff = min(min_diff, diff)
        y2 = y+1
        diff = abs(x*x + y2*y2 - D)
        min_diff = min(min_diff, diff)
        if y > 0:
            diff = abs(x*x + (y-1)*(y-1) - D)
            min_diff = min(min_diff, diff)

print(min_diff)