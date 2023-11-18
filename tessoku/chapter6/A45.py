from collections import defaultdict

N, C = input().split()
N = int(N)
A = list(input())

# dict_A = defaultdict(lambda: 0)
# for a in A:
#     dict_A[a] += 1

# while dict_A['R'] > 1 or dict_A['B'] > 1 or dict_A['W'] > 1:
#     if dict_A['R'] > 1:
#         dict_A['R'] -= 2
#         dict_A['B'] += 1
#     if dict_A['B'] > 1:
#         dict_A['B'] -= 2
#         dict_A['R'] += 1
#     if dict_A['W'] > 1:
#         dict_A['W'] -= 1

# num_cards = dict_A['R'] + dict_A['B'] + dict_A['W']
# if num_cards == 1:
#     if dict_A[C] == 1:
#         print('Yes')
#         exit()
# elif num_cards == 2:
#     if C == 'R':
#         if dict_A['W'] == 1 and dict_A['R'] == 1:
#             print('Yes')
#             exit()
#     elif C == 'B':
#         if dict_A['W'] == 1 and dict_A['B'] == 1:
#             print('Yes')
#             exit()
#     elif C == 'W':
#         if dict_A['R'] == 1 and dict_A['B'] == 1:
#             print('Yes')
#             exit()
#     print('No')
# elif num_cards == 3:
#     if C == 'W':
#         print('Yes')
#         exit()
#     print('No')

# 色毎にスコアを設定し、スコアの法則に気づけるかがポイント
score = 0
for a in A:
    if a == 'B':
        score += 1
    elif a == 'R':
        score += 2
score %= 3
colors = ['W', 'B', 'R']
if colors[score] == C:
    print('Yes')
else:
    print('No')