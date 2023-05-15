import numpy as np

a, b, c = map(int, input().split())
if c == 1:
    print('No')
    exit()
else:
    _c = 1
    for i in range(b):
        _c *= c
        if a < _c:
            print('Yes')
            exit()
    print('No')
