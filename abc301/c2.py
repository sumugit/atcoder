from collections import Counter

def can_win(S: str, T: str) -> bool:
    # 文字列SとTをそれぞれの文字に分割し、出現回数をカウントする
    counter_S = Counter(S)
    counter_T = Counter(T)

    # '@' の数をそれぞれ計算する
    at_S = counter_S.get('@', 0)
    at_T = counter_T.get('@', 0)

    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in ['a', 't', 'c', 'o', 'd', 'e', 'r']:
            if counter_S.get(char, 0) != counter_T.get(char, 0):
                return False

        diff = counter_S.get(char, 0) - counter_T.get(char, 0)
        if diff > 0:
            at_S -= diff
        elif diff < 0:
            at_T += diff

        if at_S < 0 or at_T < 0:
            return False

    return True

# 使用例
S = "atcoder@"
T = "@tcodera"
print(can_win(S, T))  # True を返すべき