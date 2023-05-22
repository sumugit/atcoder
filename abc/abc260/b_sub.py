N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dict_A = {k+1:A[k] for k in range(N)}
dict_B = {k+1:B[k] for k in range(N)}
dict_sum = {k+1:A[k]+B[k] for k in range(N)}

list_ipt = []
ans = []

for n in range(N):
    result = {'A':A[n], 'B':B[n], 'sum': A[n]+B[n]}
    id = N - n
    dict_AB = {'result':result, 'id':id}
    list_ipt.append(dict_AB)

print(list_ipt)


sort_A = sorted(list_ipt, key=lambda x:(x['result']['A'], x['id']), reverse=True)
for x in range(X):
    ans.append(N - sort_A[x]['id'] + 1)
for x in range(X):
    sort_A.pop(0)

sort_B = sorted(sort_A, key=lambda x:(x['result']['B'], x['id']), reverse=True)
for y in range(Y):
    ans.append(N - sort_B[y]['id'] + 1)
for y in range(Y):
    sort_B.pop(0)

sort_Z = sorted(sort_B, key=lambda x:(x['result']['sum'], x['id']), reverse=True)
for z in range(Z):
    ans.append(N - sort_Z[z]['id'] + 1)

ans.sort()

for a in ans:
    print(a)
