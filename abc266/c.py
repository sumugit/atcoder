import math
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

def inner(ax, ay, bx, by):
    return ax*bx + ay*by

def l1(ax, ay):
    return math.sqrt(ax**2 + ay**2)

cosA = inner(Bx-Ax, By-Ay, Dx-Ax, Dy-Ay)/(l1(Bx-Ax, By-Ay)*l1(Dx-Ax, Dy-Ay))
deg_A = math.degrees(math.acos(cosA))
cosB = inner(Ax-Bx, Ay-By, Cx-Bx, Cy-By)/(l1(Ax-Bx, Ay-By)*l1(Cx-Bx, Cy-By))
deg_B = math.degrees(math.acos(cosB))
cosC = inner(Bx-Cx, By-Cy, Dx-Cx, Dy-Cy)/(l1(Bx-Cx, By-Cy)*l1(Dx-Cx, Dy-Cy))
deg_C = math.degrees(math.acos(cosC))
cosD = inner(Ax-Dx, Ay-Dy, Cx-Dx, Cy-Dy)/(l1(Ax-Dx, Ay-Dy)*l1(Cx-Dx, Cy-Dy))
deg_D = math.degrees(math.acos(cosD))
if math.isclose(deg_A + deg_B + deg_C + deg_D, 360):
    print('Yes')
else:
    print('No')