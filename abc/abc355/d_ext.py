from sortedcontainers import SortedList

N=int(input())
LR=[tuple(map(int,input().split())) for _ in range(N)]
LR.sort()

ans=0
S=SortedList()
for l,r in LR[::-1]:
	ans+=S.bisect_right(r)
	S.add(l)
print(ans)