S = input()
T = input()
i = 0
j = 0
while j < len(S):
    if T[0] == S[j]:
        if T == S[j:j+len(T)]:
            print('Yes')
            exit()
    j+=1
print('No')