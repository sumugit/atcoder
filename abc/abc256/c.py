import itertools
import numpy as np

h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0

h1_list = list(range(1, h1))
combis = itertools.combinations(h1_list, 2)
for combi in combis:
    box = np.zeros(shape=(3, 3), dtype=int)
    # 1行目
    box[0, 0] = combi[0]
    box[0, 1] = combi[1] - combi[0]
    box[0, 2] = h1 - combi[1]
    if (box[0, 0] >= w1) or (box[0, 1] >= w2) or (box[0, 2] >= w3):
        continue
    h2_list = list(range(1, h2))
    combis2 = itertools.combinations(h2_list, 2)
    for combi2 in combis2:
        # 2行目
        box[1, 0] = combi2[0]
        box[1, 1] = combi2[1] - combi2[0]
        box[1, 2] = h2 - combi2[1]
        if (box[0, 0] + box[1, 0] >= w1) or (box[0, 1] + box[1, 1] >= w2) or (box[0, 2] + box[1, 2] >= w3):
            continue
        elif (w1 - box[0, 0] - box[1, 0]) + (w2 - box[0, 1] - box[1, 1]) + (w3 - box[0, 2] - box[1, 2]) == h3:
            ans += 1

print(ans)