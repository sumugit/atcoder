N = int(input())
S = [input() for _ in range(N)]

s_dict = {}
for s_i in S:
    s_dict.setdefault(s_i, 0)
    if s_dict[s_i] == 0:
        print(s_i)
    else:
        print(f"{s_i}({s_dict[s_i]})")
    s_dict[s_i] += 1