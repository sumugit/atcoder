N = int(input())
S = input()

a = S.count('o')
c = S.count('x')
if a>=1 and c==0:
    print('Yes')
else:
    print('No')