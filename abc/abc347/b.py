S = input()

ans_dict = {}
for i in range(len(S)+1):
    for j in range(len(S)):
        if S[j:j+i] != '' and S[j:j+i] not in ans_dict:
            ans_dict[S[j:j+i]] = True
print(len(ans_dict))