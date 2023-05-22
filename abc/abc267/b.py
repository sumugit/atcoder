from itertools import combinations

S = list(input())
S = [int(s) for s in S]

if S[0] != 0:
    print('No')
else:
    pin = [[S[6]], [S[3]], [S[7], S[1]], [S[4], S[0]], [S[8], S[2]], [S[5]], [S[9]]]
    pin_idx = range(7)
    for comb in combinations(pin_idx, 2):
        col_1 = comb[0]
        col_2 = comb[1]
        if sum(pin[col_1])>0 and sum(pin[col_2])>0:
            flag = True
            flag2 = False
            for col in range(col_1+1, col_2):
                flag2 = True
                if sum(pin[col])>0:
                    flag = False
                    break
            if flag and flag2:
                print('Yes')
                exit()
    print('No')
