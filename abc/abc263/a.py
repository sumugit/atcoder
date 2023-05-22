from collections import defaultdict

abcde = list(map(int, input().split()))
ans_dict = defaultdict(lambda: 0)
for item in abcde:
    ans_dict[item] += 1

if len(ans_dict) != 2:
    print('No')
else:
    val_sum = 0
    for key, val in ans_dict.items():
        if 2 <= ans_dict[key] <= 3:
            val_sum += ans_dict[key]
    if val_sum == 5:
        print('Yes')
    else:
        print('No')

