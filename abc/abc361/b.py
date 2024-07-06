a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

x1_min, x1_max = min(a, d), max(a, d)
y1_min, y1_max = min(b, e), max(b, e)
z1_min, z1_max = min(c, f), max(c, f)

x2_min, x2_max = min(g, j), max(g, j)
y2_min, y2_max = min(h, k), max(h, k)
z2_min, z2_max = min(i, l), max(i, l)

x_overlap = not (x1_max <= x2_min or x2_max <= x1_min)
y_overlap = not (y1_max <= y2_min or y2_max <= y1_min)
z_overlap = not (z1_max <= z2_min or z2_max <= z1_min)

if x_overlap and y_overlap and z_overlap and (x1_max-x1_min)*(y1_max-y1_min)*(z1_max-z1_min)>0 and (x2_max-x2_min)*(y2_max-y2_min)*(z2_max-z2_min)>0:
    print('Yes')
else:
    print('No')