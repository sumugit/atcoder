N = int(input())

max_num = 0
for i in range(1, 10**6+1):
    tmp = i**3
    str_tmp = str(tmp)
    if str_tmp == str_tmp[::-1] and tmp <= N:
        max_num = max(max_num, tmp)

print(max_num)