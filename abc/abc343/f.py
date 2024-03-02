from collections import defaultdict
from dataclasses import dataclass

from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))


@dataclass
class Cell:
    v1: int
    c1: int
    v2: int
    c2: int


# 問題に適合した segtree の op を定義
def op(a: Cell, b: Cell) -> Cell:
    if a.v1 == b.v1:
        if a.v2 == b.v2:
            return Cell(a.v1, a.c1 + b.c1, a.v2, a.c2 + b.c2)
        # 2番目に大きい値は常に a.v2 になるようにする
        if a.v2 < b.v2:
            a, b = b, a
        return Cell(a.v1, a.c1 + b.c1, a.v2, a.c2)
    # 1番目に大きい値は常に a.v1 になるようにする
    if a.v1 < b.v1:
        a, b = b, a
    # 2番目に大きい値は常に a.v2 になるようにする
    if a.v2 > b.v1:
        return a
    # a の 2番目に大きい値が b の 1番目に大きい値と等しい場合
    if a.v2 == b.v1:
        return Cell(a.v1, a.c1, a.v2, a.c2 + b.c1)
    return Cell(a.v1, a.c1, b.v1, b.c1)


e_ = Cell(-1, 0, -1, 0)

Acell = [Cell(x, 1, -1, 0) for x in A]
st = SegTree(op, e_, Acell)

for i in range(Q):
    t, u, v = map(int, input().split())
    if t == 1:
        st.set(u - 1, Cell(v, 1, -1, 0))
    elif t == 2:
        c = st.prod(u - 1, v)
        print(c.c2)
