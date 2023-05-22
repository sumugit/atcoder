S = input()
for i in range(len(S)):
    if S[len(S)-i-1] == 'a':
        print(len(S)-i)
        exit()
print(-1)