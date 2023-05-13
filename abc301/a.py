N = int(input())
S = input()

t = S.count('T')
a = S.count('A')
if t > a:
    print('T')
elif t < a:
    print('A')
else:
    if S[-1] == 'T':
        print('A')
    else:
        print('T')