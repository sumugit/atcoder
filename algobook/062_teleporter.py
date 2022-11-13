N, K = map(int, input().split())
A = [-1] + list(map(int, input().split()))

# 閉路内の index を参照するのが難しいので, 各 k 毎に閉路内 (2週目) にいるかどうかを判定
first = [-1]*(N+1)
second = [-1]*(N+1)
cnt = 0; cur = 1
first[cur] = 0
while True:
    next_cur = A[cur]
    cnt += 1
    if first[next_cur] == -1:
        first[next_cur] = cnt
    else:
        second[next_cur] = cnt
    if second[next_cur] != -1 and (K-cnt)%(second[next_cur]-first[next_cur]) == 0:
        ans = next_cur
        break
    elif cnt == K:
        ans = next_cur
        break
    cur = next_cur
#print(first)
#print(second)
print(ans)