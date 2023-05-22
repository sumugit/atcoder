import math

A, B = map(int, input().split())
x = (A/(2*B))**(2/3) - 1
x = int(x+1)
ans = B*x + (A/math.sqrt(1+x))
print(ans)