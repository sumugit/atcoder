import numpy as np
from itertools import combinations

H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]


""" １つでも一致しない場合の処理は関数作った方が良い """
def check(hidx,widx):
	for i in range(H2):
		for j in range(W2):
			if A[hidx[i]][widx[j]]!=B[i][j]:
				return False
	return True

for hidx in combinations(range(H1), H2):
    for widx in combinations(range(W1), W2):
        if check(hidx, widx):
            print('Yes')
            exit()
print('No')
