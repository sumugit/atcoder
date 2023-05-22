H, M = map(int, input().split())

for m in range(60-M):
        hour = H
        minute = M+m
        rep_h = 10*(hour//10) + minute//10
        rep_m = 10*(hour%10) + minute%10
        if 0<=rep_h<=23 and 0<=rep_m<=59:
            print(hour, minute)
            exit()

H = (H+1)%24
M = 0

for h in range(24):
    for m in range(60):
        hour = (H+h)%24
        minute = (M+m)%60
        rep_h = 10*(hour//10) + minute//10
        rep_m = 10*(hour%10) + minute%10
        if 0<=rep_h<=23 and 0<=rep_m<=59:
            print(hour, minute)
            exit()
