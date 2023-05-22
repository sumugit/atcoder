import sys
def input():
  return sys.stdin.readline().rstrip()
from bisect import bisect_left as bile

H,W,rs,cs=map(int,input().split())
N=int(input())
xn,yn={},{} #xn[x]はx行目、yn[y]はy列目に存在する障害物
xs,ys=set(),set() #xs,ysは障害物のない行、列
for i in range(N):
  x,y=map(int,input().split())
  xs.add(x); ys.add(y)
  xn.setdefault(x,[]); xn[x].append(y)
  yn.setdefault(y,[]); yn[y].append(x)

for i in xn.keys():
  xn[i].sort()
for i in yn.keys():
  yn[i].sort()

Q=int(input())
x,y=rs,cs #現在地
dl = []
for i in range(Q):
  dl.append(list(input().split()))
for i in range(Q):
  d,l=dl[i][0], dl[i][1]; l=int(l)
  
  if d=="L":
    if x not in xs:
      y-=l
    else:
      ind=bile(xn[x],y)-1
      if ind==-1: #左に障害物がない
        y-=l
      else:
        y=max(y-l,xn[x][ind]+1)
  elif d=="R":
    if x not in xs:
      y+=l
    else:
      ind=bile(xn[x],y)
      if ind==len(xn[x]): #右に障害物がない
        y+=l
      else:
        y=min(y+l,xn[x][ind]-1)
  elif d=="U":
    if y not in ys:
      x-=l
    else:
      ind=bile(yn[y],x)-1
      if ind==-1: #上に障害物がない
        x-=l
      else:
        x=max(x-l,yn[y][ind]+1)
  else:
    if y not in ys:
      x+=l
    else:
      ind=bile(yn[y],x)
      if ind==len(yn[y]): #下に障害物がない
        x+=l
      else:
        x=min(x+l,yn[y][ind]-1)
  x=max(1,min(x,H))
  y=max(1,min(y,W))
  print(x,y)