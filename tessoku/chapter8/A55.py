from sortedcontainers import SortedSet

class CardQueries:
    def __init__(self):
        self.cards = SortedSet()

    def add_card(self, x):
        """クエリ1: カードxを追加する"""
        self.cards.add(x)

    def remove_card(self, x):
        """クエリ2: カードxを削除する"""
        self.cards.discard(x)

    def query_min_card(self, x):
        """クエリ3: x以上のカードのうち最小のものを返す。存在しない場合はNoneを返す"""
        idx = self.cards.bisect_left(x)
        if idx < len(self.cards):
            return self.cards[idx]
        return None

# インスタンスの作成とクエリのテスト
Q = int(input())
query = [list(input().split()) for _ in range(Q)]

cq = CardQueries()
for q in query:
    num, x = q
    if num == "1":
        cq.add_card(int(x))
    elif num == "2":
        cq.remove_card(int(x))
    else:
        ans = cq.query_min_card(int(x))
        if ans is None:
            print(-1)
        else:
            print(ans)