N, Q = map(int, input().split())
query = [list(input().split()) for _ in range(Q)]

# セグメント木（ここでは書籍とは異なり、pos が 0-indexed になるように実装しています）
class segtree:
	# 要素 dat の初期化を行う（最初は全部ゼロ）
	def __init__(self, n):
		self.size = 1
		while self.size < n:
			self.size *= 2
		self.dat = [ 0 ] * (self.size * 2)
	
	# クエリ 1 に対する処理
	def update(self, pos, x):
		pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
		self.dat[pos] = x
		while pos >= 2:
            # 親の更新
			pos //= 2
			self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1]
	
	# クエリ 2 に対する処理
	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return 0 # 一切含まれない場合
		if l <= a and b <= r:
			return self.dat[u] # 完全に含まれる場合
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2) # 左の子
		answerr = self.query(l, r, m, b, u * 2 + 1) # 右の子
		return answerl + answerr

z = segtree(N)
for q in query:
    tq, *cont = q
    if tq == '1':
        pos, x = cont
        z.update(int(pos)-1, int(x))
    elif tq == '2':
        l, r = cont
        print(z.query(int(l)-1, int(r)-1, 0, z.size, 1))