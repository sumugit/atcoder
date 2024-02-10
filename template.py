from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import math
import numpy as np

def isprime(n: int) -> bool:
    """ 素数判定 """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0: return False
    return True

def gcd(a: int, b: int) -> int:
    """ 2 数の最大公約数 : ユークリッドの互除法 """
    while b:
        a, b = b, a % b
    return a

def gcd_multi(A: list) -> int:
    """ N (> 1) 個の最大公約数 """
    gcd_next = gcd(A[0], A[1])
    for i in range(len(A)-2):
        gcd_next = gcd(gcd_next, A[i+2])
    return gcd_next

def lcm(a: int, b: int) -> int:
    """ 2 数の最小公倍数 : gcd 利用 """
    return a // gcd(a, b) * b

def lcm_multi(A: list) -> int:
    """ N (> 1) 個の最小公倍数 """
    lcm_next = lcm(A[0], A[1])
    for i in range(len(A)-2):
        lcm_next = lcm(lcm_next, A[i+2])
    return lcm_next

def eratosthenes(N: int) -> list:
    """ N 以下の素数を全て求める (エラトステネスの篩) """
    P = [True] * N
    P[0] = False
    for i in range(2, int(math.sqrt(N)+1)):
        for j in range(i+1, N+1): 
            if j%i == 0:
                P[j-1] = False
    ans = []
    for i in range(1, len(P)):
        if P[i]:
            ans.append(i+1)
    return ans

def modpow(a: int, b: int, m: int, lim: int) -> int:
    """ 
    繰り返し二乗法 O(logb)
    a^b を mod で割った余りを出力
    lim : mod で割る数を2進数にした時の桁数 (10^3 ~ 2^10)
    """
    p = a
    ans = 1
    for i in range(lim):
        # bを2進数に変換して, i 桁目が 1 かどうかを判定
        if b & (1 << i) != 0:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

def division(a: int, b: int, m, lim: int) -> int:
    """
    a÷b mod m を返す関数
    フェルマーの小定理を使う
    """
    return (a*modpow(b, m-2, m, lim))%m

def binary_search(data: list, value: int) -> int:
    """ 二分探索 
    data は sort されている必要あり
    """
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1

def matrix_power(A: np.array, n: int, mod: int, lim: int) -> np.array:
    """ A^n を繰り返し二乗法で計算 """
    P = A.copy()
    Q = np.zeros(shape=(2,2))
    flag = False
    for i in range(lim):
        if n & (1 << i) != 0:
            if not flag:
                Q = P.copy()
                flag = True
            else:
                Q = (Q@P)%mod
        P = (P@P)%mod
    return Q

def binary_search(data: list, value: int) -> int:
    """ 二分探索 
    data は sort されている必要あり
    """
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1


class UnionFind:
    """ Union Find Tree """
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # 根は -1*(集合のノード数)

    def find(self, x):
        """ 根を参照するまで再帰 """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """ 木の連結 """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        # 大きい集合に小さい集合を merge
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """ ノード数の取得 """
        return -self.parents[self.find(x)]



def dijkstra(N: int, M: int, ABC: list) -> list:
    """ ダイクストラ法 """
    # 距離が最小の頂点から確定させていけば、絶対に最短経路が求まる
    graph = defaultdict(lambda: [])
    for i in range(len(ABC)):
        graph[ABC[i][0]].append((ABC[i][1], ABC[i][2]))

    kakutei = [False] * (N+1)
    cur = [float('inf')] * (N+1)
    cur[1] = 0
    q = []
    heappush(q, (cur[1], 1))

    # ダイクストラ法
    while len(q) > 0:
        # 未確定頂点の中でcurの値が最も小さい頂点posを求める
        # 優先度付きキューを使うと、O(logN)で最小値を取り出せる
        dist, pos = heappop(q)
        if kakutei[pos]:
            continue
        kakutei[pos] = True
        
        # 頂点pos に隣接する頂点について、curの値を更新する (DP)
        for i in range(len(graph[pos])):
            next_v = graph[pos][i][0]
            next_dis = graph[pos][i][1]
            if cur[next_v] > cur[pos] + next_dis:
                cur[next_v] = cur[pos] + next_dis
                heappush(q, (cur[next_v], next_v))
    return cur