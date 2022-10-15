# 外積を使う. (if, for だけの思考になるな.)
def cross(ax, ay, bx, by):
	return ax * by - ay * bx

# 変数のまま受け取った方が混乱しにくい
X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())
X4, Y4 = map(int, input().split())

# cross の値を計算
cross_abac = cross(X2-X1, Y2-Y1, X3-X1, Y3-Y1)  #ab, ac
cross_abad = cross(X2-X1, Y2-Y1, X4-X1, Y4-Y1)  #ab, ad
cross_cdca = cross(X4-X3, Y4-Y3, X1-X3, Y1-Y3)  #cd, ca
cross_cdcb = cross(X4-X3, Y4-Y3, X2-X3, Y2-Y3)  #cd, cb

# すべて一直線上に並んでいる場合（コーナーケース）
if cross_abac==cross_abad==cross_cdca==cross_cdcb == 0:
	# 適切に swap することで A<B, C<D を仮定できる
	# そうすると、区間が重なるかの判定（節末問題 2.5.6）に帰着できる
	A = (X1, Y1) # 点 A の座標
	B = (X2, Y2) # 点 B の座標
	C = (X3, Y3) # 点 C の座標
	D = (X4, Y4) # 点 D の座標
	if A > B:
		tmp = B
		B = A
		A = tmp
	if C > D:
		tmp = D
		D = C
		C = tmp
	if max(A, C) <= min(B, D):
		print("Yes")
	else:
		print("No")
else:
    if cross_abac*cross_abad <= 0 and cross_cdca*cross_cdcb <= 0:
        print("Yes")
    else:
        print("No")