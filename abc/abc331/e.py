N, M, L = map(int, input().split())
main_dishes = list(map(int, input().split()))
side_dishes = list(map(int, input().split()))

# 主菜と副菜の最高価格を見つける
max_main = max(main_dishes)
max_side = max(side_dishes)

# 食べ合わせが悪い組み合わせの処理
bad_combinations = set()
for _ in range(L):
    c, d = map(lambda x: int(x) - 1, input().split())
    bad_combinations.add((c, d))

# 最も高価な組み合わせを見つける
max_price = max_main + max_side
for c, d in bad_combinations:
    if main_dishes[c] == max_main and side_dishes[d] == max_side:
        # 次に高い価格の組み合わせを見つける
        next_max_main = max(x for i, x in enumerate(main_dishes) if i != c)
        next_max_side = max(x for i, x in enumerate(side_dishes) if i != d)
        max_price = max(max_price, next_max_main + max_side, max_main + next_max_side)

print(max_price)