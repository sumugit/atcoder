from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

card_list = sorted(A, reverse=True)[:3]
max_val = 0
for comb in permutations(card_list, 3):
    val = str(comb[0]) + str(comb[1]) + str(comb[2])
    max_val = max(max_val, int(val))

print(max_val)