N,x,y=map(int,input().split())
A=list(map(int,input().split()))

DPx=[set() for _ in range(N+1)]; DPy=[set() for _ in range(N+1)]
DPx[1]={A[0]}
DPy[0]={0}
for i in range(N):
    if i%2==0:
        # y については前の結果をコピー
        DPy[i+1]=DPy[i]
        for j in DPx[i]:
            # 足し引きして得られる数をsetに追加している
            DPx[i+1].add(j-A[i])
            DPx[i+1].add(j+A[i])
    else:
        # x については前の結果をコピー
        DPx[i+1]=DPx[i]
        for j in DPy[i]:
            DPy[i+1].add(j-A[i])
            DPy[i+1].add(j+A[i])

if x in DPx[N] and y in DPy[N]:
    print("Yes")
else:
    print("No")