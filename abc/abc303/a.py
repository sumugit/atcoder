N = int(input())
S = input()
T = input()

for i in range(N):
    if (S[i] == T[i]) or (S[i] == '1' and T[i] == 'l') or (S[i] == 'l' and T[i] == '1') or (S[i] == '0' and T[i] == 'o') or (S[i] == 'o' and T[i] == '0'):
        continue
    else:
        print('No')
        exit()
print('Yes')