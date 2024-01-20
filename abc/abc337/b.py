S = list(input())

ans_str = ''
for i in range(len(S)-1):
    if S[i] == S[i+1] and i != len(S)-2:
        continue
    elif S[i] == S[i+1] and i == len(S)-2:
        ans_str += S[i]
    else:
        ans_str += S[i]

if len(S) > 1 and S[-1] != S[-2]:
    ans_str += S[-1]

if ans_str in 'ABC' or ans_str in 'AC':
    print('Yes')
else:
    print('No')