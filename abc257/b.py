import numpy as np

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

mass = np.zeros(N, dtype=int)
for i in range(len(A)):
    mass[A[i]-1] = i + 1

for i in range(len(L)):
        
    for j in range(len(mass)):
        if mass[j] == L[i]:
            if j != N - 1:
                if mass[j+1] == 0:
                    mass[j+1] = mass[j]
                    mass[j] = 0
            break

ans = []

for i in range(len(mass)):
    if mass[i] > 0:
        ans.append(i+1)

print(*ans)