from collections import Counter, deque, defaultdict

N = int(input())
S = list(input())

str_dict = defaultdict(lambda: 0)

length = 1
temp = ''
if len(S) == 1:
    print(1)
    exit()
for i in range(N-1):
    temp = S[i]
    if S[i] == S[i+1]:
        length += 1
    else:
        str_dict[temp] = max(str_dict[temp], length)
        temp = ''
        length = 1

temp = S[-1]
str_dict[temp] = max(str_dict[temp], length)
print(str_dict)
ans = 0
for key in str_dict.keys():
    ans += str_dict[key]
print(ans)
