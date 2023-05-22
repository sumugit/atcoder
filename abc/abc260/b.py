import pandas as pd

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

list_AB = [[k+1, A[k], B[k]] for k in range(N)]
df = pd.DataFrame(list_AB, columns=['num', 'A', 'B'])

ans = []

df = df.sort_values(by=['A', 'num'], ascending=[False, True]).reset_index(drop=True)
df['sum'] = df['A'] + df['B']

print(df.head())

for x in range(X):
    # print(df.iloc[x:x+1]['num'].values[0])
    ans.append(df.iloc[x:x+1]['num'].values[0])

df = df.iloc[X:]
df = df.sort_values(by=['B', 'num'], ascending=[False, True]).reset_index(drop=True)

# print(df.head())

for y in range(Y):
    # print(df.iloc[y:y+1]['num'].values[0])
    ans.append(df.iloc[y:y+1]['num'].values[0])

df = df.iloc[Y:]
df = df.sort_values(by=['sum', 'num'], ascending=[False, True]).reset_index(drop=True)

# print(df.head())

for z in range(Z):
    # print(df.iloc[z:z+1]['num'].values[0])
    ans.append(df.iloc[z:z+1]['num'].values[0])

ans.sort()

for a in ans:
    print(a)
