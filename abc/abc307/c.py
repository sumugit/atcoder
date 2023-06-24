# H_A, W_A = map(int, input().split())
# A = [list(input()) for _ in range(H_A)]
# H_B, W_B = map(int, input().split())
# B = [list(input()) for _ in range(H_B)]
# H_X, W_X = map(int, input().split())
# X = [list(input()) for _ in range(H_X)]

# B_1 = [(i, j) for i in range(H_B) for j in range(W_B) if B[i][j] == '#']
# X_1 = [(i, j) for i in range(H_X) for j in range(W_X) if X[i][j] == '#']

# C = set()
# for i in range(H_A):
#     for j in range(W_A):
#         if A[i][j] == '#':
#             C.add((i+10, j+10))

# for i in range(30-H_B+1):
#     for j in range(30-W_B+1):
#         D = C.copy()
#         for b in B_1:
#             D.add((i+b[0], j+b[1]))
#         for k in range(30-H_X+1):
#             for l in range(30-W_X+1):
#                 E = set()
#                 for x in X_1:
#                     E.add((k+x[0], l+x[1]))
#                 if D == E:
#                     print('Yes')
#                     exit()
# print('No')

def convert(H, W, S):
    s = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                s.add((i, j))
    return s

def normalize(s):
    my = min(y for (y, x) in s)
    mx = min(x for (y, x) in s)
    return set((y - my, x - mx) for (y, x) in s)

HA, WA = map(int, input().split())
A = normalize(convert(HA, WA, [input() for _ in range(HA)]))
HB, WB = map(int, input().split())
B = normalize(convert(HB, WB, [input() for _ in range(HB)]))
HX, WX = map(int, input().split())
X = normalize(convert(HX, WX, [input() for _ in range(HX)]))
ans = False
for dy in range(-HX, HX):
    for dx in range(-WX, WX):
        # 標準化するからマイナスでも0以上になる
        ans |= normalize(A.union((y + dy, x + dx) for (y, x) in B)) == X
print('Yes' if ans else 'No')

