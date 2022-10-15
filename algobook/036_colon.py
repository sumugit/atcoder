import math
A, B, H, M = map(int, input().split())

rad_H = (0.5*60*H + 0.5*M)%360
rad_M = (6*M)%360

delta = min(abs(rad_H-rad_M), 360-abs(rad_H-rad_M))
# print(delta)
ans_2 = A**2 + B**2 - 2*A*B*math.cos(delta/180*math.pi)
ans = math.sqrt(ans_2)
print(ans)