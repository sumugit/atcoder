# PyPy3 (7.3.0)
N = int(input())
A = list(map(int, input().split()))

ans_cnt = 0

dict_a = {i:0 for i in range(1, 100000)}
for a in A:
    dict_a[a] += 1

for i in range(1, 50000):
    ans_cnt += dict_a[i]*dict_a[100000-i]

sub = dict_a[50000]
if sub > 1:
    ans_cnt += int((sub*(sub-1))/2)
print(ans_cnt)

