import math

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
X = sorted(points, key=lambda x:x[0])  # x 座標でソート
Y = sorted(points, key=lambda x:x[1])  # y 座標でソート


# 2 次元空間内の点同士の距離を求める
def distance(a: list, b: list) -> float:
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

# 最小距離を求める
def compute_closest_pairs(input_list):
    if len(input_list) < 2: return 10**9
    delta = 10**9
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            dist = distance(input_list[i], input_list[j])
            delta = min(delta, dist)
    return delta

# 最小距離となる点を分割統治法で求める
def closestPoint(X: list, Y: list) -> float:
    # X : x 座標でソートした座標リスト
    # Y : y 座標でソートした座標リスト
    n = len(X)
    if n < 3: return compute_closest_pairs(X)
    x_median = int(n/2)
    # 右半分, 左半分に分割
    X_l = []
    X_r = []
    Y_l = []
    Y_r = []
    for point in X:
        if point[0] <= X[x_median][0]: X_l.append(point)
        else: X_r.append(point)
    
    if X == X_l or X == X_r:
        X_l = X[:x_median]
        X_r = X[x_median:]
    
    for point in Y:
        if point in X_l:
            Y_l.append(point)
        else:
            Y_r.append(point)
    
    delta = 10**9
    # (X_l, Y_l), (X_r, Y_r) は座標集合としては同じだが, ソートされている軸が異なる
    delta_l = closestPoint(X_l, Y_l)
    delta_r = closestPoint(X_r, Y_r)
    delta = min(delta_l, delta_r)
    Y_d = []
    for point in Y:
        if abs(X[x_median][0] - point[0]) ** 2 < delta:
            Y_d.append(point)
    Y_d_len = len(Y_d)
    for i in range(Y_d_len):
        for j in range(i+1, Y_d_len):
            temp_dis = distance(Y_d[i], Y_d[j])
            delta = min(delta, temp_dis)
    
    return delta

ans = math.sqrt(closestPoint(X, Y))
print(ans)