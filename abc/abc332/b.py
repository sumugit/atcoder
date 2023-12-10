K, G, M = map(int, input().split())

v_g = 0
v_m = 0
for _ in range(K):
    if v_g == G:
        v_g = 0
    elif v_m == 0:
        v_m = M
    else:
        rest = G - v_g
        if rest > v_m:
            v_g += v_m
            v_m = 0
        else:
            v_g = G
            v_m -= rest

print(v_g, v_m)