S = input()
T = input()

conf = T[:len(S)]
if S == conf:
    print('Yes')
else:
    print('No')