N = int(input())
S = input()

l = []
dot = -1
for i in range(N):
    if S[i] == '|':
        l.append(i)
    elif S[i] == '*':
        dot = i
if l[0] < dot < l[1]:
    print('in')
else:
    print('out')