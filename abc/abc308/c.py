from functools import cmp_to_key

def cmp(idx_ab0, idx_ab1):
    idx0, ab0 = idx_ab0
    idx1, ab1 = idx_ab1
    # 比較対象の分数 a と b が等しければ 0 を返す
    if ab0[0] * (ab1[0] + ab1[1]) == ab1[0] * (ab0[0] + ab0[1]):
        return idx1 - idx0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if ab0[0] * (ab1[0] + ab1[1]) < ab1[0] * (ab0[0] + ab0[1]) else 1

N = int(input())
AB = [[i, list(map(int, input().split()))] for i in range(N)]
AB = sorted(AB, key=cmp_to_key(cmp))
indices = [AB[i][0]+1 for i in range(N)]
indices = indices[::-1]
print(*indices)