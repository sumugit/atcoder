p, q = input().split()
alp_dict = {
    'A': 0,
    'B': 3,
    'C': 4,
    'D': 8,
    'E': 9,
    'F': 14,
    'G': 23,
    }
ans = abs(alp_dict[p] - alp_dict[q])
print(ans)