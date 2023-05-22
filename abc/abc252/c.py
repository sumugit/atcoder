"""
N = int(input())
S = []
for _ in range(N):
    S.append(input())

n_time = []

for n in range(10):
    s_time = []
    max_num = -1
    max_cnt = 0
    # 位置が重複している文字の数
    for i in range(len(S)):
        num = S[i].find(str(n))
        if num in s_time and num > max_num:
            max_num = num
            max_cnt = 1
        elif num in s_time and num == max_num:
            max_cnt += 1
        s_time.append(num)
            
    n_max = max(s_time)
    if max_cnt > 0:
        n_time.append(n_max + (10 - (n_max - max_num)) +  10 * (max_cnt - 1))
    else:
        n_time.append(n_max)

print(min(n_time))
"""

n=int(input())
s=[]
for i in range(n):
	s.append(input())

cnt=[[0 for j in range(10)]for i in range(10)]
for i in range(n):
	for j in range(10):
		cnt[int(s[i][j])][j]= cnt[int(s[i][j])][j]+1

mx=[0 for i in range(10)]
for i in range(10):
	for j in range(10):
		mx[i]=max(mx[i], 10 * (cnt[i][j] - 1) + j)

print(min(mx))
