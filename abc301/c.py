from collections import defaultdict

S = input().strip()
T = input().strip()

atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']
a_dict = defaultdict(int)
b_dict = defaultdict(int)

for s, t in zip(S, T):
    a_dict[s] += 1
    b_dict[t] += 1

a_rest = a_dict['@']
b_rest = b_dict['@']

for key in set(a_dict.keys()).union(b_dict.keys()):
    if key == '@':
        continue
    if a_dict[key] < b_dict[key]:
        if a_rest > 0 and key in atcoder:
            a_rest -= b_dict[key] - a_dict[key]
            if a_rest < 0:
                print('No')
                exit()
        else:
            print('No')
            exit()
    elif a_dict[key] > b_dict[key]:
        if b_rest > 0 and key in atcoder:
            b_rest -= a_dict[key] - b_dict[key]
            if b_rest < 0:
                print('No')
                exit()
        else:
            print('No')
            exit()
print('Yes')