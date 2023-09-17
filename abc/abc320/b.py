S = input()

max_len = 1
for i in range(len(S)):
    for j in range(i+1, len(S)):
        if S[i:j+1] == S[i:j+1][::-1]:
            max_len = max(max_len, j-i+1)
print(max_len)