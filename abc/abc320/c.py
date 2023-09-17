import re

M = int(input())
S1 = input()
S2 = input()
S3 = input()

min_time = 10**9
for num in range(10):
    # num の位置を探す
    pos_s1 = [i.start() for i in re.finditer(str(num), S1)]
    pos_s2 = [i.start() for i in re.finditer(str(num), S2)]
    pos_s3 = [i.start() for i in re.finditer(str(num), S3)]
    # 3つの位置の組み合わせを全探索
    for i in range(len(pos_s1)):
        for j in range(len(pos_s2)):
            for k in range(len(pos_s3)):
                time_to_stop_s1 = pos_s1[i]
                time_to_stop_s2 = pos_s2[j]
                time_to_stop_s3 = pos_s3[k]
                time_to_stop_s1, time_to_stop_s2, time_to_stop_s3 = sorted([time_to_stop_s1, time_to_stop_s2, time_to_stop_s3])
                if time_to_stop_s1 == time_to_stop_s2 == time_to_stop_s3:
                    min_time = min(min_time, time_to_stop_s1 + 2*M)
                elif time_to_stop_s1 == time_to_stop_s2:
                    min_time = min(min_time, time_to_stop_s1 + M)
                elif time_to_stop_s2 == time_to_stop_s3:
                    min_time = min(min_time, time_to_stop_s2 + M)
                else:
                    min_time = min(min_time, time_to_stop_s3)
if min_time == 10**9:
    print(-1)
else:
    print(min_time)
        