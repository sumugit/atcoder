from itertools import combinations

N = int(input())
N_bin_lst = list(map(int, list(bin(N)[2:])))
N_bin_idx = [idx for idx in range(len(N_bin_lst)) if N_bin_lst[idx] == 1]
cnt_1 = sum(N_bin_lst)

ans_lst = []

for k in range(cnt_1+1):
    for comb in combinations(N_bin_idx, k):
        temp = ['0'] * len(N_bin_lst)
        for idx in comb:
            temp[idx] = '1'
        ans_lst.append(int(''.join(temp), 2))

ans_lst = sorted(ans_lst)
for val in ans_lst:
    print(val)