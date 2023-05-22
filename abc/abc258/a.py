K = int(input())

h = 21 + int(K/60)
m = K%60
if m < 10:
    m = '0' + str(K%60)
else:
    m = str(K%60)

print(f'{h}:{m}')