import numpy as np
a, b, d = map(int, input().split())

vec_a = np.array([a, b])
A = np.array([[np.cos(np.radians(d)), -np.sin(np.radians(d))],
                [np.sin(np.radians(d)), np.cos(np.radians(d))]])

vec_b = A@vec_a

print(vec_b[0], vec_b[1])