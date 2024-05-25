N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]


def count_intersecting_intervals(intervals):    
    # Step 1: 座標圧縮
    endpoints = []
    for l, r in intervals:
        endpoints.append(l)
        endpoints.append(r)
        
    endpoints = sorted(set(endpoints))
    coord_map = {v: i for i, v in enumerate(endpoints)}    
    compressed_intervals = [(coord_map[l], coord_map[r]) for l, r in intervals]
    
    # Step 2: 累積和
    cnt = []
    for l, r in compressed_intervals:
        cnt.append((l, 1))
        cnt.append((r, 2))
    # 0 番目が同じ場合は start が先に来るようにする
    cnt = sorted(cnt, key=lambda x: (x[0], x[1]))
    
    num_start = 0
    ans = 0
    for i in range(len(cnt)):
        # start
        if cnt[i][1] == 1:
            ans += num_start
            num_start += 1
        # end
        else:
            num_start -= 1
    
    return ans

print(count_intersecting_intervals(lr))