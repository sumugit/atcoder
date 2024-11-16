S = input()
s_arr = S.split('|')
ans = [len(s) for s in s_arr if len(s) > 0]
print(*ans)