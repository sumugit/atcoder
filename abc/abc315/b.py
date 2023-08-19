M = int(input())
D = list(map(int, input().split()))

middle = (sum(D)+1) // 2
sum_D = []
for i in range(M):
    sum_D.append(sum(D[:i+1]))

month = 0
for i in range(M):
    if sum_D[i] >= middle:
        month = i
        break

month += 1
day = middle - sum_D[month-2]
if month == 1:
    day = middle
print(month, day)