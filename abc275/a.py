import numpy as np
N = int(input())
H = list(map(int, input().split()))

print(np.argmax(H)+1)